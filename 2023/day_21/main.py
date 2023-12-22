def run():
    with open("input.txt") as f:
        lines = f.read().splitlines()

        grid = []
        start = None
        for i, line in enumerate(lines):
            row = list(line)
            grid.append(row)
            if "S" in row:
                start = (i, row.index("S"))

        x_max = len(grid)
        y_max = len(grid[0])
        positions = set([start])

        res = [(0, 1)]
        # for i in range(1, 328):
        #     next_positions = set()
        #     for x, y in list(positions):
        #         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #             nx, ny = x + dx, y + dy

        #             # if nx < 0 or nx >= x_max or ny < 0 or ny >= y_max:
        #             #     continue

        #             # if grid[nx][ny] not in ".S":
        #             if grid[nx % x_max][ny % y_max] not in ".S":
        #                 continue

        #             next_positions.add((nx, ny))
        #     res.append((i, len(next_positions)))
        #     positions = next_positions

        for i in range(len(res)):
            curr = res[i]
            if curr[0] in [65, 196, 327]:
                print(curr)

        f_0 = 3911
        f_1 = 34786
        f_2 = 96435
        c = f_0
        b = int(2 * f_1 - (3 / 2) * f_0 - (1 / 2) * f_2)
        a = int((1 / 2) * f_2 - f_1 + (1 / 2) * f_0)

        n = 202300
        print(a, b, c)
        print(a * n**2 + b * n + c)


if __name__ == "__main__":
    run()
    # f(x) = a*x**2 + b*x + c
    # f(0) = fill(HALF) = fill(65) = 3911
    # f(1) = fill(HALF + size) = fill(65 + 131) = fill(196) = 34786
    # f(2) = fill(HALF + 2*size) = fill(65 + 262) = fill(327) = 96435
    # f(0) = c
    # f(1) = a + b + f(0)
    #    b = f(1) - f(0) - a
    # f(2) = 4a + 2b + c = 4a + 2(f(1) - f(0) - a) + f(0) = 4a + 2f(1) - 2f(0) - 2a + f(0)
    # f(2) = 2a + 2f(1) - f(0)
    #   a  = f(2)/2 - f(1) + f(0)/2
    #   b  = f(1) - f(0) - (f(2)/2 - f(1) + f(0)/2) = 2f(1) - 3/2f(0) - f(2)/2
    #   c  = f(0)
    # fill(26501365) = fill(HALF + 202300*size) = f(202300)
