

def solver(grid, entry, exit, visited=None, path=None):

    # base cases
    if visited is None:
        visited = set()

    if path is None:
        path = []

    if entry == exit:
        path.append(entry)
        return True, path

    visited.add(entry)
    path.append(entry)

    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    # for every neighbor, call recursion to check if base case is true
    for direction, (dx, dy) in directions.items():
        if not entry.walls[direction]:
            neighbor = grid[entry.y + dy][entry.x + dx]
            if neighbor not in visited:
                if solver(grid, neighbor, exit, visited, path):
                    return True, path

    #removes last element from list
    path.pop()
    return False, path
