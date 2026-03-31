from config_checker import ConfigChecker
from maze_algorithm import generate_maze, print_maze
from solver import solver
from output_generator import output
from colorama import Fore
from itertools import cycle
from time import sleep
from sys import argv
import os


def menu() -> None:

    """Interface and main function"""

    if len(argv) != 2 or argv[1] != "config.txt":
        print("Usage: python3 a_maze_ing.py config.txt")
        return

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
    print_maze(grid, entry, exit, path, visible, maze_color, color42)

    print("\n****** A-MAZE-ING ******")
    print("1 - Regenerate a maze\n2 - Change colors\n3 - Toggle path\n"
          "4 - Change color 42\n5 - Disco Mode\n6 - Clear terminal\n"
          "0 - Exit")

    option = int(input("\nEnter option: "))

    try:
        while True:

            if option < 0 or option > 6:
                print("Please input a valid choice.")
                option = int(input("\nEnter option: "))

            if option == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                grid, entry, exit = generate_maze(config, maze_color, color42)
                path = solver(grid, entry, exit)
                output(grid, path, entry, exit, output_name)
                print_maze(grid, entry, exit, path, visible,
                            maze_color, color42)

            elif option == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                maze_color = next(colors)
                print_maze(grid, entry, exit, path, visible,
                            maze_color, color42)

            elif option == 3:
                if visible is True:
                    visible = False

                elif visible is False:
                    visible = True
                os.system('cls' if os.name == 'nt' else 'clear')
                print_maze(grid, entry, exit, path, visible,
                            maze_color, color42)

            elif option == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                color42 = next(colors42)
                print_maze(grid, entry, exit, path, visible,
                            maze_color, color42)

            elif option == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                for _ in range(100):
                    color42 = next(colors42)
                    print_maze(grid, entry, exit, path, visible,
                                maze_color, color42)
                    sleep(0.04)
                    maze_color = next(colors)
                    print_maze(grid, entry, exit, path, visible,
                                maze_color, color42)
                    sleep(0.04)
            elif option == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                return print("\nProgram finished successfully!\n")

            print("\n****** A-MAZE-ING ******")
            print("1 - Regenerate a maze\n2 - Change colors\n3 - Toggle path\n"
                    "4 - Change color 42\n5 - Disco Mode\n6 - Clear terminal\n"
                    "0 - Exit")

            if option == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n****** A-MAZE-ING ******")
                print("1 - Regenerate a maze\n2 - Change colors\n3 - Toggle path\n"
                        "4 - Change color 42\n5 - Disco Mode\n6 - Clear terminal\n"
                        "0 - Exit")

            option = int(input("\nEnter option: "))

    except Exception:
        print("An error has occured.")


if __name__ == "__main__":
    menu()
