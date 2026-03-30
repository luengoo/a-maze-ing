from config_checker import ConfigChecker
from maze_algorithm import generate_maze, print_maze
from solver import solver
from output_generator import output
from colorama import Fore
from itertools import cycle
from time import sleep
from sys import argv


def menu():

    if len(argv) != 2 or argv[1] != "config.txt":
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    try:
        checker = ConfigChecker()
        config = checker.opener()
        output_name = config.get("OUTPUT_FILE")

        maze_color, color42 = Fore.WHITE, Fore.WHITE
        visible = False

        grid, entry, exit = generate_maze(config, maze_color, color42)
        path = solver(grid, entry, exit)
        output(grid, path, entry, exit, output_name)

        colors = cycle((Fore.GREEN, Fore.YELLOW, Fore.WHITE))
        colors42 = cycle((Fore.BLUE, Fore.MAGENTA, Fore.WHITE))
        print_maze(grid, entry, exit, path, visible, maze_color, color42, finished=False)

        while True:
            option = int(input("\nEnter option: "))

            if option == 1:
                grid, entry, exit = generate_maze(config, maze_color, color42)
                path = solver(grid, entry, exit)
                output(grid, path, entry, exit, output_name)
                print_maze(grid, entry, exit, path, visible, maze_color, color42, finished=False)

            elif option == 2:
                maze_color = next(colors)
                print_maze(grid, entry, exit, path, visible, maze_color, color42, finished=False)

            elif option == 3:
                if visible is True:
                    visible = False

                elif visible is False:
                    visible = True
                print_maze(grid, entry, exit, path, visible, maze_color, color42, finished=False)

            elif option == 4:
                color42 = next(colors42)
                print_maze(grid, entry, exit, path, visible, maze_color, color42, finished=False)

            elif option == 5:
                for _ in range(100):
                    color42 = next(colors42)
                    print_maze(grid, entry, exit, path, visible, maze_color, color42, finished=False)
                    sleep(0.04)
                    maze_color = next(colors)
                    print_maze(grid, entry, exit, path, visible, maze_color, color42, finished=False)
                    sleep(0.04)

    except Exception as e:
        print(f"An error has been found. Please check config.txt.", e)


if __name__ == "__main__":
    menu()
