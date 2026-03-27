from collections import deque


# bfs algo
def solver(grid, entry, exit):

    # optimazation
    parent = {entry: None}

    q = deque([entry])
    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    while q:
        current = q.popleft()

        if current == exit:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
                path.reverse()
            return path

        for direction, (dx, dy) in directions.items():
            if not current.walls[direction]:
                neighbor = grid[current.y + dy][current.x + dx]
                if neighbor not in parent:
                    parent[neighbor] = current
                    q.append(neighbor)

    return None