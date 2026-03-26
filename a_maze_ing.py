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
    print_maze(grid, entry, exit, path, visible, maze_color, finished=False)

    while True:
        option = int(input("\nEnter option: "))

        if option == 1:
            grid, entry, exit = generate_maze(config)
            success, path = solver(grid, entry, exit, path=None)
            os.system("cls" if os.name == "nt" else "clear")
            print_maze(grid, entry, exit, path, visible, maze_color, finished=False)

        elif option == 2:
            os.system("cls" if os.name == "nt" else "clear")
            print_maze(grid, entry, exit, path, visible, maze_color, finished=False)
            pass

        elif option == 3:
            os.system("cls" if os.name == "nt" else "clear")
            if visible is True:
                visible = False
            
            elif visible is False:
                visible = True

            print_maze(grid, entry, exit, path, visible, maze_color, finished=False)

        elif option == 4:

            # change color 
            pass
    


def main():

    menu()


if __name__ == "__main__":
    main()
