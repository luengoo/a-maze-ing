from config_checker import ConfigChecker
from maze_algorithm import generate_maze, print_maze
import os

if __name__ == "__main__":
    checker = ConfigChecker()
    config = checker.opener()

    grid, entry, exit = generate_maze(config)

    os.system("cls" if os.name == "nt" else "clear")
    print_maze(grid, entry, exit)
