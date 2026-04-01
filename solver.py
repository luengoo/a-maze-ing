from collections import deque
from maze_algorithm import Cell


def solver(grid: list[list[Cell]], entry: Cell, exit: Cell) -> (
            list[Cell] | None):

    """BFS Algorithm. Performant algorithm for maze solving with
        perfect and non-perfect mazes"""

    # optimization
    parent: dict[Cell, Cell | None] = {entry: None}

    q = deque([entry])
    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    while q:
        current: Cell | None = q.popleft()

        if current == exit:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        for direction, (dx, dy) in directions.items():
            if current is None:
                continue
            if not current.walls[direction]:
                neighbor = grid[current.y + dy][current.x + dx]
                if neighbor not in parent:
                    parent[neighbor] = current
                    q.append(neighbor)

    return None
