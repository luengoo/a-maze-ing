from config_checker import ConfigChecker
from maze_algorithm import generate_maze, print_maze
from solver import solver
import os


def menu(config):
       
    print("\n---------------MENU------------------")
    print("1 - Regenerate a maze | 2 - Change colors | 3 - Hide path | 4 - Change color 42")

    option = int(input("Enter option: "))

    if option is 1:
        grid, entry, exit = generate_maze(config)
        os.system("cls" if os.name == "nt" else "clear")
        print_maze(grid, entry, exit)

    elif option is 2:

        # maze color
        pass
    
    elif option is 3:

        # path toggle
        pass
    
    elif option is 4:

        # change color 
        pass
    


def main():
    checker = ConfigChecker()
    config = checker.opener()

    grid, entry, exit = generate_maze(config)

    os.system("cls" if os.name == "nt" else "clear")
    print_maze(grid, entry, exit)
    while True:
        menu(config)


if __name__ == "__main__":
    main()