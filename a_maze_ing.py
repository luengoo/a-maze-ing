from config_checker import ConfigChecker
from maze_algorithm import generate_maze, print_maze
from solver import solver
import os


def menu():

    checker = ConfigChecker()
    config = checker.opener()

    grid, entry, exit = generate_maze(config)
    success, path = solver(grid, entry, exit, path=None)
    os.system("cls" if os.name == "nt" else "clear")

    visible = False
    maze_color = None
    print_maze(grid, entry, exit, path, visible, maze_color)

    while True:
        print("\n****** A-MAZE-ING ******")
        print("1 - Regenerate a maze\n2 - Change colors\n3 - Hide path\n4 - Change color 42")

        option = int(input("Enter option: "))

        if option is 1:
            grid, entry, exit = generate_maze(config)
            success, path = solver(grid, entry, exit, path=None)
            os.system("cls" if os.name == "nt" else "clear")
            print_maze(grid, entry, exit, path, visible, maze_color)

        elif option is 2:
            os.system("cls" if os.name == "nt" else "clear")
            print_maze(grid, entry, exit, path, visible, maze_color)
            pass

        elif option is 3:
            os.system("cls" if os.name == "nt" else "clear")
            if visible is True:
                visible = False
            
            elif visible is False:
                visible = True

            print_maze(grid, entry, exit, path, visible, maze_color)

        elif option is 4:

            # change color 
            pass
    


def main():

    menu()


if __name__ == "__main__":
    main()
