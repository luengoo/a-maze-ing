from colorama import Fore, Style
import random
import time
from typing import Optional, Any
import os


class Cell:
    """class that represents a cell of the maze"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = False
        self.blocked = False
        self.walls: dict[str, bool] = {"N": True,
                                       "E": True,
                                       "S": True,
                                       "W": True}


def create_grid(width: int, height: int) -> list[list[Cell]]:
    """creates full grid"""
    return [[Cell(x, y) for x in range(width)] for y in range(height)]


def get_neighbors(cell: Cell, grid: list[list[Cell]],
                  include_blocked: bool = False) -> list[Cell]:
    """get the neighboring cells of a cell"""
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


def remove_wall(a: Cell, b: Cell) -> None:
    """removes wall cell"""
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


def print_maze(grid: list[list[Cell]], entry: Optional[Cell],
               exit: Optional[Cell], path: Optional[list[Cell]],
               visible: bool, maze_color: str, color42: str) -> None:
    """perfect maze creation algorithm"""
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


def imperfect_maze(grid: list[list[Cell]]) -> None:
    """randomly removes walls using a removal rate"""
    limit = 0.15
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cell = grid[y][x]
            if cell.walls["E"] and x + 1 < len(grid[0]):
                if random.random() < limit:
                    cell.walls["E"] = False
                    grid[y][x + 1].walls["W"] = False
            if cell.walls["S"] and y + 1 < len(grid):
                if random.random() < limit:
                    cell.walls["S"] = False
                    grid[y + 1][x].walls["N"] = False


def prim_maze(grid: list[list[Cell]], maze_color: str, color42: str,
              perfect: bool) -> None:
    """Perfect maze generation algorithm"""
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
        visited_neighbors: list[Cell] = []
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

        os.system('clear')
        print_maze(grid, entry=None, exit=None, path=None, visible=False,
                   maze_color=maze_color, color42=color42)
        cell.visited = True

        for n in get_neighbors(cell, grid):
            if not n.visited and n not in frontier:
                frontier.append(n)

    if not perfect:
        imperfect_maze(grid)
        print_maze(grid, entry=None, exit=None, path=None, visible=False,
                   maze_color=maze_color, color42=color42)


def set_entry_exit(grid: list[list[Cell]], entry: tuple[int, int],
                   exit: tuple[int, int]) -> tuple[Cell, Cell]:
    """get the entry and exit cells on the grid"""
    eny, enx = entry
    exy, exx = exit
    entry_cell = grid[eny][enx]
    exit_cell = grid[exy][exx]
    return entry_cell, exit_cell


def generate_maze(config: dict[str, Any], maze_color: str,
                  color42: str) -> tuple[list[list[Cell]], Cell, Cell]:
    """orchestrates the maze generation"""

    random.seed(config.get("SEED"))

    perfect = config.get("PERFECT")
    width = int(config.get("WIDTH", 20))
    height = int(config.get("HEIGHT", 10))

    grid = create_grid(width, height)
    draw_42(grid)
    prim_maze(grid, maze_color, color42, bool(perfect))

    entry_tuple = config.get("ENTRY")
    exit_tuple = config.get("EXIT")

    entry, exit = set_entry_exit(grid, entry_tuple,  # type: ignore
                                 exit_tuple)  # type: ignore

    return grid, entry, exit


def draw_42(grid: list[list[Cell]]) -> None:
    """set the 42 pattern on the grid"""
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
