from heapq import heappush, heappop


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        grid = []
        for line in lines:
            grid.append([int(e) for e in list(line)])
        size = len(grid)
        target = (size - 1, size - 1)

        h = []
        heappush(h, (grid[0][1], set("0:0"), [((0, 1), "RIGHT")]))
        heappush(h, (grid[1][0], set("0:0"), [((1, 0), "DOWN")]))
        while h:
            distance, visited, path = heappop(h)
            (coord, _) = path[-1]
            x, y = coord

            if x < 0 or x >= size or y < 0 or y >= size:
                continue

            if str(x) + ":" + str(y) in visited:
                continue

            visited.add(str(x) + ":" + str(y))

            if coord == target:
                print(path)
                print(distance)
                break

            for next_direction in directions(path):
                if next_direction == "LEFT":
                    next_x, next_y = x, y - 1
                    if next_y >= 0:
                        heappush(
                            h,
                            (
                                distance + grid[next_x][next_y],
                                visited,
                                path + [((next_x, next_y), next_direction)],
                            ),
                        )

                if next_direction == "DOWN":
                    next_x, next_y = x + 1, y
                    if next_x < size:
                        heappush(
                            h,
                            (
                                distance + grid[next_x][next_y],
                                visited,
                                path + [((next_x, next_y), next_direction)],
                            ),
                        )

                if next_direction == "UP":
                    next_x, next_y = x - 1, y
                    if next_x >= 0:
                        heappush(
                            h,
                            (
                                distance + grid[next_x][next_y],
                                visited,
                                path + [((next_x, next_y), next_direction)],
                            ),
                        )

                if next_direction == "RIGHT":
                    next_x, next_y = x, y + 1
                    if next_y < size:
                        heappush(
                            h,
                            (
                                distance + grid[next_x][next_y],
                                visited,
                                path + [((next_x, next_y), next_direction)],
                            ),
                        )


def directions(path):
    next_directions = []
    current_direction = path[-1][1]
    if current_direction == "LEFT":
        next_directions += ["UP", "DOWN"]

    if current_direction == "DOWN":
        next_directions += ["RIGHT", "LEFT"]

    if current_direction == "RIGHT":
        next_directions += ["DOWN", "UP"]

    if current_direction == "UP":
        next_directions += ["LEFT", "RIGHT"]

    if len(path) < 3:
        next_directions += [current_direction]
    else:
        if len(set([path[-1][1], path[-2][1], path[-3][1]])) > 1:
            next_directions += [current_direction]

    return next_directions


if __name__ == "__main__":
    run()
