import random
import time
import os


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"N": True, "E": True, "S": True, "W": True}


def create_grid(width, height):
    return [[Cell(x, y) for x in range(width)] for y in range(height)]


def get_neighbors(cell, grid):
    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    neighbors = []
    for dx, dy in directions.values():
        nx, ny = cell.x + dx, cell.y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            neighbors.append(grid[ny][nx])
    return neighbors


def remove_wall(a, b):
    dx = b.x - a.x
    dy = b.y - a.y

    if dx == 1:
        a.walls["E"] = False
        b.walls["W"] = False
    elif dx == -1:
        a.walls["W"] = False
        b.walls["E"] = False
    elif dy == 1:
        a.walls["S"] = False
        b.walls["N"] = False
    elif dy == -1:
        a.walls["N"] = False
        b.walls["S"] = False


def print_maze(grid, entry, exit):
    height = len(grid)
    width = len(grid[0])

    for y in range(height):
        for x in range(width):
            print("+", end="")
            print("---" if grid[y][x].walls["N"] else "   ", end="")
        print("+")

        for x in range(width):
            print("|" if grid[y][x].walls["W"] else " ", end="")

            if grid[y][x] == entry:
                print(" E ", end="")
            elif grid[y][x] == exit:
                print(" X ", end="")
            else:
                print("   ", end="")

        print("|")

    for x in range(width):
        print("+---", end="")
    print("+")


def draw(grid, entry=None, exit=None):
    os.system("cls" if os.name == "nt" else "clear")
    print_maze(grid, entry, exit)
    time.sleep(0.05)


def prim_maze(grid, draw_step=None):
    height = len(grid)
    width = len(grid[0])

    start = grid[random.randint(0, height-1)][random.randint(0, width-1)]
    start.visited = True

    frontier = get_neighbors(start, grid)

    if draw_step:
        draw_step(grid)

    while frontier:
        cell = random.choice(frontier)
        frontier.remove(cell)

        visited_neighbors = [n for n in get_neighbors(cell, grid) if n.visited]

        if visited_neighbors:
            neighbor = random.choice(visited_neighbors)
            remove_wall(cell, neighbor)

            cell.visited = True

            for n in get_neighbors(cell, grid):
                if not n.visited and n not in frontier:
                    frontier.append(n)

            if draw_step:
                draw_step(grid)


def set_entry_exit(grid, entry, exit):
    eny, enx = entry
    exy, exx = exit

    entry_cell = grid[eny][enx]
    exit_cell = grid[exy][exx]

    entry_cell.walls["N"] = False
    exit_cell.walls["S"] = False

    return entry_cell, exit_cell


def generate_maze(config):
    random.seed(config.get("SEED"))

    width = int(config.get("WIDTH", 20))
    height = int(config.get("HEIGHT", 10))

    grid = create_grid(width, height)

    prim_maze(grid, draw_step=draw)

    entry_tuple = config.get("ENTRY", "0,0")
    exit_tuple = config.get("EXIT", "0,0")

    entry, exit = set_entry_exit(grid, entry_tuple, exit_tuple)

    return grid, entry, exit


if __name__ == "__main__":
    from config_checker import ConfigChecker

    checker = ConfigChecker()
    config = checker.opener()

    grid, entry, exit = generate_maze(config)

    os.system("cls" if os.name == "nt" else "clear")
    print_maze(grid, entry, exit)
