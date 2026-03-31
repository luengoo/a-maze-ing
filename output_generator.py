
def output(grid: list[list], path: list, entry: tuple, exit: tuple, output_name: str) -> None:

    """Writes the hexadecimal maze representation and
     the path's steps into output_name.txt"""

    height = len(grid)
    width = len(grid[0])

    directions = []

    for i in range(len(path) - 1):
        x1, y1 = path[i].x, path[i].y
        x2, y2 = path[i + 1].x, path[i + 1].y

        if x2 == x1 + 1:
            directions.append('E')
        elif x2 == x1 - 1:
            directions.append('W')
        elif y2 == y1 + 1:
            directions.append('S')
        elif y2 == y1 - 1:
            directions.append('N')

    path_string = ''.join(directions)

    with open(output_name, "w") as f:
        for y in range(height):
            for x in range(width):
                value = grid[y][x].walls[
                    "W"] * 8 + grid[y][x].walls["S"] * 4 + grid[y][x].walls[
                        "E"] * 2 + grid[y][x].walls["N"] * 1
                value = format(value, 'X')
                f.write(value)
            f.write("\n")

        f.write(f"\n{entry.x}, {entry.y}\n")
        f.write(f"{exit.x}, {exit.y}\n")
        f.write(f"{path_string}")

