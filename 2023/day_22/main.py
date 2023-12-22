from collections import defaultdict
from heapq import heappush, heappop
import numpy as np


def run():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        bricks = []
        x_max, y_max, z_max = 0, 0, 0
        for i, line in enumerate(lines):
            start, end = line.split("~")
            start = tuple(map(int, start.split(",")))
            end = tuple(map(int, end.split(",")))

            x_max = max(x_max, start[0] + 1, end[0] + 1)
            y_max = max(y_max, start[1] + 1, end[1] + 1)
            z_max = max(z_max, start[2] + 1, end[2] + 1)
            bricks.append((i + 1, start, end))
            # bricks.append((chr(i + 65), start, end))

        size = x_max * y_max * z_max
        space = np.array([0] * (size)).reshape(x_max, y_max, z_max)

        h = []
        for b in bricks:
            z = min(b[1][2], b[2][2])
            heappush(h, (z, b))

        while h:
            _, b = heappop(h)
            b_name, b_start, b_end = b

            for i in range(3):
                assert b_start[i] <= b_end[i]

            if b_start[2] == b_end[2]:
                (x_start, y_start, z) = b_start
                (x_end, y_end, _) = b_end

                for k in range(z, -1, -1):
                    if np.any(space[x_start : x_end + 1, y_start : y_end + 1, k] != 0):
                        k += 1
                        break

                space[x_start : x_end + 1, y_start : y_end + 1, k] = b_name

            else:
                assert b_start[0] == b_end[0] and b_start[1] == b_end[1]

                (x, y, z) = b_start
                for k in range(z, -1, -1):
                    if space[x, y, k] != 0:
                        k += 1
                        break

                delta_z = z - k
                space[x, y, k : b_end[2] - delta_z + 1] = b_name

        supports = defaultdict(set)
        for i in range(x_max):
            for j in range(y_max):
                for k in range(z_max - 1):
                    current = space[i, j, k]
                    above = space[i, j, k + 1]
                    if current != 0 and above != 0 and current != above:
                        supports[current].add(above)

        supported_by = defaultdict(set)
        for support, above in supports.items():
            for supported in above:
                supported_by[supported].add(support)

        # print(space[:, :, 0])

        # print(supports)
        # print(supported_by)

        res = 0
        for b in bricks:
            b_name = b[0]

            if len(supports[b_name]) == 0:
                res += 1
            else:
                if all(len(supported_by[elem]) > 1 for elem in supports[b_name]):
                    res += 1

        print(res)


if __name__ == "__main__":
    run()
