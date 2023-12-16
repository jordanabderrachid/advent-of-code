import numpy as np


def run():
    with open("input.txt") as f:
        patterns = f.read().split("\n\n")

        summary = 0
        for pattern in patterns:
            lines = []
            for line in pattern.split("\n"):
                lines.append(np.array(list(line)))

            grid = np.stack(lines)
            for i in range(0, grid.shape[0]):
                if horizontal_symmetry(grid, i):
                    summary += 100 * (i + 1)

            for j in range(0, grid.shape[1]):
                if vertical_symmetry(grid, j):
                    summary += j + 1

        print(summary)


def horizontal_symmetry(grid, d):
    line_count = grid.shape[0]
    if d == line_count - 1:
        return False

    difference_count = 0
    for i in range(0, min(d + 1, line_count - d - 1)):
        difference_count += (grid[d - i] != grid[d + i + 1]).sum()

    return difference_count == 1


def vertical_symmetry(grid, d):
    col_count = grid.shape[1]
    if d == col_count - 1:
        return False

    difference_count = 0
    for j in range(0, min(d + 1, col_count - d - 1)):
        difference_count += (grid[:, d - j] != grid[:, d + j + 1]).sum()

    return difference_count == 1


if __name__ == "__main__":
    run()
