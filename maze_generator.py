from parsing import ConfigChecker, check_terminal_size
from output_generator import output
from maze_algorithm import generate_maze, print_maze
from solver import solver
import os


class CreateMaze():
    """Maze creation class"""
    def __init__(self, visible, maze_color, color42):
        self.visible = visible
        self.maze_color = maze_color
        self.color42 = color42
        self.grid = None
        self.path = None
        self.entry = None
        self.exit = None

    def create_maze(self) -> bool:
        """Creates the maze after calling the parser, return True if success"""
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            checker = ConfigChecker()
            config = checker.opener()
        except (ValueError, FileNotFoundError) as e:
            print(f"Found an error in config.txt file: {e}")
            return False

        try:
            check_terminal_size(int(config.get("WIDTH")),
                                int(config.get("HEIGHT")))
        except RuntimeError as e:
            print(f"An error has been found: {e}")
            return False

        output_name = config.get("OUTPUT_FILE")
        self.grid, self.entry, self.exit = generate_maze(
            config, self.maze_color, self.color42)

        self.path = solver(self.grid, self.entry, self.exit)
        output(self.grid, self.path, self.entry, self.exit, output_name)

        return True

    def display_maze(self):
        """calls print_maze"""
        print_maze(self.grid, self.entry, self.exit, self.path,
                   self.visible, self.maze_color, self.color42)
