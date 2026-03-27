from collections import deque

def solver(grid, entry, exit, visited=False, path=None):

    visited = set()
    rows, cols = len(grid), len(grid[0])

    q = deque()
    q.append([entry])
    
    visited.add((entry.y, entry.x))

    directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]

    while q:
        path = q.popleft()
        current = path[-1]

        if current.x == exit.x and current.y == exit.y:
            pass

        for dy, dx in directions:
            ny, nx = current.y + dy, current.x + dx

            if (0 <= nx < rows and 0 <= ny < cols and
                grid[ny][nx] == 0 and (ny, nx) not in visited):
                visited.add((ny, nx))
                neighbor = grid[ny][nx]
                q.append(path + neighbor)
        return None