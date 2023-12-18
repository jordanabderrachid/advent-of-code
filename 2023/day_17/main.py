from heapq import heappush, heappop


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        grid = []
        for line in lines:
            grid.append([int(e) for e in list(line)])
        size = len(grid)
        target = (size - 1, size - 1)

        visited = set()
        # heat, x, y, dx, dy, consecutive_step_in_direction
        h = [(0, 0, 0, 0, 0, 0)]
        while h:
            heat, x, y, dx, dy, count = heappop(h)
            if (x, y, dx, dy, count) in visited:
                continue

            visited.add((x, y, dx, dy, count))

            if (x, y) == target and count >= 4:
                print(heat)
                break

            if count < 10 and (dx, dy) != (0, 0):
                # we can continue going in that direction
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size:
                    heappush(h, (heat + grid[nx][ny], nx, ny, dx, dy, count + 1))

            if count >= 4 or (dx, dy) == (0, 0):
                # now we check all the other directions (N, E, S, W)
                for ndx, ndy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    # if we are not going in the same direction, or oposite direction
                    # ie only left, right turns
                    if (ndx, ndy) != (dx, dy) and (ndx, ndy) != (-dx, -dy):
                        nx, ny = x + ndx, y + ndy
                        if 0 <= nx < size and 0 <= ny < size:
                            heappush(h, (heat + grid[nx][ny], nx, ny, ndx, ndy, 1))


if __name__ == "__main__":
    run()
