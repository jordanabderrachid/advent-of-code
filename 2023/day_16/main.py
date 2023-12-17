def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        grid = []
        for line in lines:
            grid.append(list(line))

        res = 0
        size = len(grid)
        for d in range(size):
            res = max(res, count_visited(0, d, "DOWN", grid))
            res = max(res, count_visited(size - 1, d, "UP", grid))
            res = max(res, count_visited(d, 0, "RIGHT", grid))
            res = max(res, count_visited(d, size - 1, "LEFT", grid))

        print(res)


def count_visited(x, y, direction, grid):
    size = len(grid)
    energized = set()
    q = [((x, y), direction)]
    while q:
        coord, direction = q.pop(0)
        x, y = coord
        if x < 0 or x >= size or y < 0 or y >= size:
            continue

        desc = str(coord[0]) + ":" + str(coord[1]) + ":" + direction
        if desc in energized:
            continue

        energized.add(desc)

        symbol = grid[x][y]
        if symbol == ".":
            if direction == "RIGHT":
                q.append(((x, y + 1), direction))
            elif direction == "DOWN":
                q.append(((x + 1, y), direction))
            elif direction == "LEFT":
                q.append(((x, y - 1), direction))
            elif direction == "UP":
                q.append(((x - 1, y), direction))

        elif symbol == "\\":
            if direction == "RIGHT":
                q.append(((x + 1, y), "DOWN"))
            elif direction == "DOWN":
                q.append(((x, y + 1), "RIGHT"))
            elif direction == "LEFT":
                q.append(((x - 1, y), "UP"))
            elif direction == "UP":
                q.append(((x, y - 1), "LEFT"))

        elif symbol == "/":
            if direction == "RIGHT":
                q.append(((x - 1, y), "UP"))
            elif direction == "DOWN":
                q.append(((x, y - 1), "LEFT"))
            elif direction == "LEFT":
                q.append(((x + 1, y), "DOWN"))
            elif direction == "UP":
                q.append(((x, y + 1), "RIGHT"))

        elif symbol == "-":
            if direction == "RIGHT":
                q.append(((x, y + 1), "RIGHT"))
            elif direction == "DOWN":
                q.append(((x, y + 1), "RIGHT"))
                q.append(((x, y - 1), "LEFT"))
            elif direction == "LEFT":
                q.append(((x, y - 1), "LEFT"))
            elif direction == "UP":
                q.append(((x, y + 1), "RIGHT"))
                q.append(((x, y - 1), "LEFT"))

        elif symbol == "|":
            if direction == "RIGHT":
                q.append(((x - 1, y), "UP"))
                q.append(((x + 1, y), "DOWN"))
            elif direction == "DOWN":
                q.append(((x + 1, y), "DOWN"))
            elif direction == "LEFT":
                q.append(((x - 1, y), "UP"))
                q.append(((x + 1, y), "DOWN"))
            elif direction == "UP":
                q.append(((x - 1, y), "UP"))

    visited = set()
    for en in energized:
        x, y, direction = en.split(":")
        visited.add(x + ":" + y)

    return len(visited)


if __name__ == "__main__":
    run()
