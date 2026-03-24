import random
import time


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
    for d, (dx, dy) in directions.items():
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


def prim_maze(grid):
    height = len(grid)
    width = len(grid[0])

    start = grid[random.randint(0, height-1)][random.randint(0, width-1)]
    start.visited = True

    frontier = get_neighbors(start, grid)

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


def set_entry_exit(grid):
    height = len(grid)
    width = len(grid[0])

    entry = grid[0][random.randint(0, width-1)]
    exit = grid[height-1][random.randint(0, width-1)]

    entry.walls["N"] = False
    exit.walls["S"] = False

    return entry, exit


def print_maze(grid, entry, exit):
    height = len(grid)
    width = len(grid[0])

    for y in range(height):
        time.sleep(0.1)
        for x in range(width):
            print("+", end="")
            if grid[y][x].walls["N"]:
                print("---", end="")
            else:
                print("   ", end="")
        print("+")

        for x in range(width):
            if grid[y][x].walls["W"]:
                print("|", end="")
            else:
                print(" ", end="")

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


def generate_maze(config):
    random.seed(config.get("SEED"))

    width = int(config.get("WIDTH", 20))
    height = int(config.get("HEIGHT", 10))

    grid = create_grid(width, height)

    prim_maze(grid)

    entry, exit = set_entry_exit(grid)

    return grid, entry, exit


if __name__ == "__main__":
    from config_checker import ConfigChecker
    checker = ConfigChecker()
    config = checker.opener()

    grid, entry, exit = generate_maze(config)
    print_maze(grid, entry, exit)
