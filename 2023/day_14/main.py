import numpy as np


def run():
    with open("input.txt") as f:
        input = f.read()

        lines = []
        for line in input.split("\n"):
            lines.append(np.array(list(line)))

        grid = np.stack(lines)
        # print(grid)
        # results = []
        iter = 159 + (1000000000 - 159) % 77
        for i in range(iter):
            grid = cycle(grid)
            # results.append(grid)
            # print("iteration", i + 1)
            # for e, result in enumerate(results[:-1]):
            # if np.all(grid == result):
            # print("match", e + 1)

            # print("---")
        print(load(grid))

        # res = 0
        # for j in range(grid.shape[1]):
        #     col = grid[:, j]
        #     rock_positions = rock_position(col.tolist())
        #     res += weight(move_rocks(rock_positions), col.shape[0])

        # print(res)


def cycle(grid):
    grid = move_north(grid)  # N
    grid = move_west(grid)
    grid = move_south(grid)
    grid = move_east(grid)
    return grid


def move_up(grid):
    cols = []
    for j in range(grid.shape[1]):
        col = grid[:, j]
        rock_positions = rock_position(col.tolist())
        cols.append(np.array(move_rocks(rock_positions, col.shape[0])))

    return np.stack(cols, axis=1)


def move_north(grid):
    return move_up(grid)


def move_west(grid):
    return move_up(grid.transpose()).transpose()


def move_south(grid):
    grid = np.flip(grid, axis=0)
    grid = move_up(grid)
    grid = np.flip(grid, axis=0)
    return grid


def move_east(grid):
    grid = grid.transpose()
    grid = np.flip(grid, axis=0)
    grid = move_up(grid)
    grid = np.flip(grid, axis=0)
    grid = grid.transpose()
    return grid


def rock_position(column):
    positions = []
    block_start = -1
    movable_count = 0
    for i, rock in enumerate(column):
        if rock == "O":
            movable_count += 1

        if rock == "#":
            positions.append((block_start, movable_count))
            block_start = i
            movable_count = 0

    positions.append((block_start, movable_count))

    return positions


def move_rocks(initial_position, length):
    positions = ["."] * length
    for start, count in initial_position:
        if start != -1:
            positions[start] = "#"
        for i in range(start + 1, start + 1 + count):
            positions[i] = "O"

    return positions


def load(grid):
    res = 0
    for j in range(grid.shape[1]):
        col = grid[:, j]
        col = col.tolist()
        size = len(col)
        for i, e in enumerate(col):
            if e == "O":
                res += size - i

    return res


if __name__ == "__main__":
    run()
