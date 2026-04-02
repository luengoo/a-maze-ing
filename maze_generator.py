from parsing import ConfigChecker, check_terminal_size
from output_generator import output
from maze_algorithm import generate_maze, print_maze, Cell
from solver import solver
from typing import Optional
import os


class CreateMaze():
    """Maze creation class"""
    def __init__(self, visible: bool, maze_color: str, color42: str) -> None:
        self.visible = visible
        self.maze_color = maze_color
        self.color42 = color42
        self.grid: Optional[list[list[Cell]]] = None
        self.path: Optional[list[Cell]] = None
        self.entry: Optional[Cell] = None
        self.exit: Optional[Cell] = None

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
            check_terminal_size(int(config.get("WIDTH")),  # type: ignore
                                int(config.get("HEIGHT")))  # type: ignore
        except RuntimeError as e:
            print(f"An error has been found: {e}")
            return False

        output_name = config.get("OUTPUT_FILE")
        self.grid, self.entry, self.exit = generate_maze(
            config, self.maze_color, self.color42)

        self.path = solver(self.grid, self.entry, self.exit)
        if self.path is None:
            self.path = []
        output(self.grid, self.path, self.entry, self.exit, str(output_name))

        return True

    def display_maze(self) -> None:
        """calls print_maze"""
        if self.grid is None:
            return
        print_maze(self.grid, self.entry, self.exit, self.path,
                   self.visible, self.maze_color, self.color42)
