from colorama import Fore, Style
import random
import time
import os


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.blocked = False
        self.walls = {"N": True, "E": True, "S": True, "W": True}


def create_grid(width, height):
    return [[Cell(x, y) for x in range(width)] for y in range(height)]


def get_neighbors(cell, grid, include_blocked=False):
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
            neighbor = grid[ny][nx]
            if not neighbor.visited and (
             include_blocked or not neighbor.blocked):
                neighbors.append(neighbor)
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


def print_maze(grid, entry, exit, path, visible, maze_color, color42, finished):
    height = len(grid)
    width = len(grid[0])

    print("\033[H", end="")
    for y in range(height):
        for x in range(width):
            print(maze_color + "+", end="")
            print("---" if grid[y][x].walls["N"] else "   ", end="")
        print("+")

        for x in range(width):

            print(maze_color + "|" if grid[y][x].walls["W"] else " ", end="")
            if grid[y][x].blocked:
                print(color42 + "###", end="")
            elif grid[y][x] == entry:
                print(maze_color + " E ", end="")
            elif grid[y][x] == exit:
                print(maze_color + " X ", end="")
            elif path and grid[y][x] in path and visible is True:
                print(Fore.RED + " * ", end="" + Style.RESET_ALL)
            else:
                print("   ", end="")

        print(maze_color + "|")

    for x in range(width):
        print("+---", end="")
    print("+" + Style.RESET_ALL)

    if not finished:
        print("\n****** A-MAZE-ING ******")
        print("1 - Regenerate a maze\n2 - Change colors\n3 - Toggle path\n4 - Change color 42\n5 - Disco Mode")



def prim_maze(grid, maze_color, color42):
    height = len(grid)
    width = len(grid[0])

    start = grid[random.randint(0, height-1)][random.randint(0, width-1)]
    while start.blocked:
        start = grid[random.randint(0, height-1)][random.randint(0, width-1)]
    start.visited = True

    frontier = get_neighbors(start, grid)

    while frontier:
        cell = random.choice(frontier)
        frontier.remove(cell)

        directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
        visited_neighbors = []
        for dx, dy in directions.values():
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                n = grid[ny][nx]
                if n.visited and not n.blocked:
                    visited_neighbors.append(n)

        if visited_neighbors:
            neighbor = random.choice(visited_neighbors)
            remove_wall(cell, neighbor)
            time.sleep(0.01)
            print_maze(grid, entry=None, exit=None, path=None, visible=False, maze_color=maze_color,color42=color42, finished=False)
            cell.visited = True

            for n in get_neighbors(cell, grid):
                if not n.visited and n not in frontier:
                    frontier.append(n)


def set_entry_exit(grid, entry, exit):
    eny, enx = entry
    exy, exx = exit

    entry_cell = grid[eny][enx]
    exit_cell = grid[exy][exx]

    return entry_cell, exit_cell


def generate_maze(config, maze_color, color42):
    random.seed(config.get("SEED"))

    width = int(config.get("WIDTH", 20))
    height = int(config.get("HEIGHT", 10))

    grid = create_grid(width, height)

    draw_42(grid)

    prim_maze(grid, maze_color, color42)

    entry_tuple = config.get("ENTRY")
    exit_tuple = config.get("EXIT")

    entry, exit = set_entry_exit(grid, entry_tuple, exit_tuple)
    print_maze(grid, entry, exit, path=None, visible=False, maze_color=maze_color, color42=color42, finished=True)

    return grid, entry, exit


def draw_42(grid):
    height = len(grid)
    width = len(grid[0])

    if height < 6 or width < 12:
        return

    start_y = height // 2 - 2
    start_x = width // 2 - 4

    pattern = [
        "#    ###",
        "#      #",
        "###  ###",
        "  #  #  ",
        "  #  ###"
    ]

    for dy in range(len(pattern)):
        for dx in range(len(pattern[dy])):
            if pattern[dy][dx] == "#":
                y = start_y + dy
                x = start_x + dx
                if 0 <= y < height and 0 <= x < width:
                    grid[y][x].blocked = True
                    grid[y][x].visited = True
