from maze_generator import MazeGenerator
from colorama import Fore
from itertools import cycle
from time import sleep
from sys import argv
import os

def menu() -> None:

    """Interface and main function"""

    if len(argv) != 2 or argv[1] != "config.txt":
        print("Usage: python3 a_maze_ing.py config.txt")

    try:
        maze_color, color42 = Fore.WHITE, Fore.WHITE
        visible = False
        generator = MazeGenerator(visible, maze_color, color42)

        colors = cycle((Fore.GREEN, Fore.YELLOW, Fore.WHITE))
        colors42 = cycle((Fore.BLUE, Fore.MAGENTA, Fore.WHITE))

        maze_color = next(colors)
        generator.update_visuals(visible, maze_color, color42)
        generator.create_maze()
        generator.display_maze()

        print("\n****** A-MAZE-ING ******")
        print("1 - Regenerate a maze\n2 - Change colors\n3 - Toggle path\n"
            "4 - Change color 42\n5 - Disco Mode\n6 - Clear terminal\n"
            "0 - Exit")
    
        option = int(input("\nEnter option: "))
        
        while True:

            if option < 0 or option > 6:
                print("Please input a valid choice.")
                option = int(input("\nEnter option: "))

            if option == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                generator.create_maze()
                generator.display_maze()

            elif option == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                generator.maze_color = next(colors)
                generator.display_maze()

            elif option == 3:
                if generator.visible is True:
                    generator.visible = False

                elif generator.visible is False:
                    generator.visible = True
                os.system('cls' if os.name == 'nt' else 'clear')
                generator.display_maze()

            elif option == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                generator.color42 = next(colors42)
                generator.display_maze()

            elif option == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                for _ in range(100):
                    generator.color42 = next(colors42)
                    generator.display_maze()
                    sleep(0.04)
                    generator.maze_color = next(colors)
                    generator.display_maze()
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
                print("1 - Regenerate a maze\n2 - Change colors\n"
                      "3 - Toggle path\n4 - Change color 42\n"
                      "5 - Disco Mode\n6 - Clear terminal\n0 - Exit")

            option = int(input("\nEnter option: "))

    except Exception:
        print("An error has been found.")


if __name__ == "__main__":
    menu()
