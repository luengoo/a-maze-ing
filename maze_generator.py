from config_checker import ConfigChecker, check_terminal_size
from output_generator import output
from maze_algorithm import generate_maze, print_maze
from solver import solver
import os

class MazeGenerator():

    def __init__(self, visible, maze_color, color42):
        self.visible = visible
        self.maze_color = maze_color
        self.color42 = color42


    def update_visuals(self, visible, maze_color, color42):
        self.visible = visible
        self.maze_color = maze_color
        self.color42 = color42


    def create_maze(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            checker = ConfigChecker()
            config = checker.opener()
        except (ValueError, FileNotFoundError) as e:
            raise(e)

        try:
            check_terminal_size(int(config.get("WIDTH")),
                                int(config.get("HEIGHT")))
        except RuntimeError as e:
            raise(e)

        output_name = config.get("OUTPUT_FILE")
        self.grid, self.entry, self.exit = generate_maze(config, self.maze_color, self.color42)
        self.path = solver(self.grid, self.entry, self.exit)
        output(self.grid, self.path, self.entry, self.exit, output_name)


    def display_maze(self):
        print_maze(self.grid, self.entry, self.exit, self.path, self.visible, self.maze_color, self.color42)
        
