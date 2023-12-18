from typing import Optional


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        start = find_start(lines)

        edge = []
        visited = set()
        stack = [coord(start)]
        while stack:
            x, y = stack.pop()
            if coords_str(x, y) in visited:
                continue

            visited.add(coords_str(x, y))
            edge.append((x, y))

            for neighbor in next_tiles((x, y), lines):
                stack.append(neighbor)

        print("part 1:", len(edge) // 2)

        corners = []
        for x, y in edge:
            if lines[x][y] in "SJLF7":
                corners.append((x, y))

        # print(corners)

        # this is the shoelace formula
        # https://en.wikipedia.org/wiki/Shoelace_formula
        A = (
            abs(
                sum(
                    [
                        corners[i][0]
                        * (corners[(i + 1) % len(corners)][1] - corners[i - 1][1])
                        for i in range(len(corners))
                    ]
                )
            )
            // 2
        )

        # this is pick's theorem
        # https://en.wikipedia.org/wiki/Pick%27s_theorem
        i = A - (len(edge) // 2) + 1
        print("part 2:", i)


def coord(v: str) -> (int, int):
    s = v.split(":")
    return (int(s[0]), int(s[1]))


def find_start(lines: list[str]) -> str:
    start = ""
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            c = lines[i][j]

            if c == "S":
                start = coords_str(i, j)

    return start


def next_tiles(
    current: tuple[int, int], grid: list[list[str]]
) -> list[tuple[int, int]]:
    x, y = current
    symbol = grid[x][y]

    res = []
    if symbol == "S":
        north = grid[x - 1][y]
        if north in "|7F":
            res.append((x - 1, y))

        east = grid[x][y + 1]
        if east in "-J7":
            res.append((x, y + 1))

        south = grid[x + 1][y]
        if south in "|JL":
            res.append((x + 1, y))

        west = grid[x][y - 1]
        if west in "-LF":
            res.append((x, y - 1))

    if symbol == "|":
        north = grid[x - 1][y]
        if north in "|7F":
            res.append((x - 1, y))

        south = grid[x + 1][y]
        if south in "|JL":
            res.append((x + 1, y))

    if symbol == "-":
        east = grid[x][y + 1]
        if east in "-J7":
            res.append((x, y + 1))

        west = grid[x][y - 1]
        if west in "-LF":
            res.append((x, y - 1))

    if symbol == "L":
        north = grid[x - 1][y]
        if north in "|7F":
            res.append((x - 1, y))

        east = grid[x][y + 1]
        if east in "-J7":
            res.append((x, y + 1))

    if symbol == "J":
        north = grid[x - 1][y]
        if north in "|7F":
            res.append((x - 1, y))

        west = grid[x][y - 1]
        if west in "-LF":
            res.append((x, y - 1))

    if symbol == "7":
        south = grid[x + 1][y]
        if south in "|JL":
            res.append((x + 1, y))

        west = grid[x][y - 1]
        if west in "-LF":
            res.append((x, y - 1))

    if symbol == "F":
        east = grid[x][y + 1]
        if east in "-J7":
            res.append((x, y + 1))

        south = grid[x + 1][y]
        if south in "|JL":
            res.append((x + 1, y))

    return res


def coords_str(i: int, j: int) -> str:
    return f"{i}:{j}"


if __name__ == "__main__":
    run()
