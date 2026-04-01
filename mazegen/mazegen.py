import random
from collections import deque
from typing import Optional


class Cell:
    """Represents a single cell in the maze grid."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = False
        self.blocked = False
        self.walls: dict[str, bool] = {"N": True,
                                       "E": True,
                                       "S": True,
                                       "W": True}


class MazeGenerator:
    """Standalone maze generator class.

    Example usage:
        gen = MazeGenerator(width=15, height=15,
                            entry=(0, 0), exit=(14, 14),
                            perfect=True, seed=42)
        gen.generate()
        grid = gen.grid
        path = gen.get_solution()
    """

    def __init__(self, width: int, height: int,
                 entry: tuple[int, int], exit: tuple[int, int],
                 perfect: bool, seed: Optional[int] = None):
        self.width = width
        self.height = height
        self.entry_coords = entry
        self.exit_coords = exit
        self.perfect = perfect
        self.seed = seed
        self.grid: Optional[list[list[Cell]]] = None
        self.entry: Optional[Cell] = None
        self.exit: Optional[Cell] = None
        self.path: Optional[list[Cell]] = None

    def generate(self) -> None:
        """Generates the maze and gets the solution path."""
        random.seed(self.seed)
        self.grid = self._create_grid()
        self._draw_42()
        self._prim_maze()
        eny, enx = self.entry_coords
        exy, exx = self.exit_coords
        self.entry = self.grid[eny][enx]
        self.exit = self.grid[exy][exx]
        self.path = self.get_solution()

    def get_solution(self) -> list[Cell]:
        """Returns the path as a list of the shortest path to the exit"""
        return self._bfs(self.entry, self.exit)

    def _create_grid(self) -> list[list[Cell]]:
        """Creates an n x n grid of cells"""
        return [[Cell(x, y)
                 for x in range(self.width)]
                for y in range(self.height)]

    def _draw_42(self) -> None:
        """set the 42 pattern on the grid"""
        if self.grid is None:
            return
        height = len(self.grid)
        width = len(self.grid[0])

        if height < 6 or width < 12:
            return

        start_y = height // 2 - 2
        start_x = width // 2 - 4

        pattern = [
            "#    ###",
            "#      #",
            "###  ###",
            "  #  #  ",
            "  #  ###"
        ]

        for dy in range(len(pattern)):
            for dx in range(len(pattern[dy])):
                if pattern[dy][dx] == "#":
                    y = start_y + dy
                    x = start_x + dx
                    if 0 <= y < height and 0 <= x < width:
                        self.grid[y][x].blocked = True
                        self.grid[y][x].visited = True

    def _prim_maze(self) -> None:
        """Perfect maze creation algorithm"""
        if self.grid is None:
            return
        grid = self.grid
        start = grid[random.randint(0, self.height - 1)][
                     random.randint(0, self.width - 1)]
        while start.blocked:
            start = grid[random.randint(0, self.height - 1)][
                         random.randint(0, self.width - 1)]
        start.visited = True
        frontier = self._get_neighbors(start)

        while frontier:
            cell = random.choice(frontier)
            frontier.remove(cell)

            visited_neighbors: list[Cell] = []
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                nx, ny = cell.x + dx, cell.y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    n = grid[ny][nx]
                    if n.visited and not n.blocked:
                        visited_neighbors.append(n)

            if visited_neighbors:
                neighbor = random.choice(visited_neighbors)
                self._remove_wall(cell, neighbor)

            cell.visited = True
            for n in self._get_neighbors(cell):
                if not n.visited and n not in frontier:
                    frontier.append(n)

        if not self.perfect:
            self._imperfect_maze()

    def _imperfect_maze(self) -> None:
        """randomly removes walls from the maze based on a removal rate"""
        if self.grid is None:
            return
        limit = 0.15
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                if cell.walls["E"] and x + 1 < self.width:
                    if random.random() < limit:
                        cell.walls["E"] = False
                        self.grid[y][x + 1].walls["W"] = False
                if cell.walls["S"] and y + 1 < self.height:
                    if random.random() < limit:
                        cell.walls["S"] = False
                        self.grid[y + 1][x].walls["N"] = False

    def _remove_wall(self, a: Cell, b: Cell) -> None:
        """remove corresponding walls from cell a and b"""
        dx = b.x - a.x
        dy = b.y - a.y
        if dx == 1:
            a.walls["E"] = False
            b.walls["W"] = False
        elif dx == -1:
            a.walls["W"] = False
            b.walls["E"] = False
        elif dy == 1:
            a.walls["S"] = False
            b.walls["N"] = False
        elif dy == -1:
            a.walls["N"] = False
            b.walls["S"] = False

    def _get_neighbors(self, cell: Cell) -> list[Cell]:
        """gets a list of neighboring cells"""
        if self.grid is None:
            return []
        neighbors = []
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                n = self.grid[ny][nx]
                if not n.visited and not n.blocked:
                    neighbors.append(n)
        return neighbors

    def _bfs(self, start: Optional[Cell],
             end: Optional[Cell]) -> list[Cell]:
        """Breadth-First Search algorithm, uses a queue,
            explores multiple paths at the same time to find the
            shortest one."""
        if start is None or end is None or self.grid is None:
            return []
        queue: deque[list[Cell]] = deque([[start]])
        visited: set[Cell] = {start}
        while queue:
            path = queue.popleft()
            cell = path[-1]
            if cell is end:
                return path
            for dx, dy, wall, _ in [
                (0, -1, "N", "S"), (1, 0, "E", "W"),
                (0, 1, "S", "N"), (-1, 0, "W", "E")
            ]:
                nx, ny = cell.x + dx, cell.y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbor = self.grid[ny][nx]
                    if neighbor not in visited and not cell.walls[wall]:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
        return []
