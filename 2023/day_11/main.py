from itertools import combinations


def run():
    with open("input.txt") as f:
        grid = [list(line) for line in f.read().split("\n")]

        empty_rows = set()
        for i, row in enumerate(grid):
            if has_no_galaxy(row):
                empty_rows.add(i)

        empty_columns = set()
        for j in range(len(grid[0])):
            column_j = []
            for i in range(len(grid)):
                column_j.append(grid[i][j])

            if has_no_galaxy(column_j):
                empty_columns.add(j)

        def distance(left: tuple[int, int], right: tuple[int, int]) -> int:
            expansion_factor = 1000000

            row_span = set(range(min(left[0], right[0]), max(left[0], right[0])))
            duplicate_row_span = empty_rows.intersection(row_span)
            duplicate_row_count = len(duplicate_row_span)
            non_duplicate_row_count = len(row_span) - duplicate_row_count

            col_span = set(range(min(left[1], right[1]), max(left[1], right[1])))
            duplicate_col_span = empty_columns.intersection(col_span)
            duplicate_col_count = len(duplicate_col_span)
            non_duplicate_col_count = len(col_span) - duplicate_col_count

            return (
                non_duplicate_row_count
                + non_duplicate_col_count
                + expansion_factor * (duplicate_row_count + duplicate_col_count)
            )

        print(empty_rows, empty_columns)
        # expanded_grid = [[] for _ in range(len(grid))]
        # for j in range(len(grid[0])):
        #     column_j = []
        #     for i in range(len(grid)):
        #         column_j.append(grid[i][j])

        #     if has_no_galaxy(column_j):
        #         for line in expanded_grid:
        #             line += [".", "."]
        #     else:
        #         for i, elem in enumerate(column_j):
        #             expanded_grid[i].append(elem)

        # grid = []
        # for line in expanded_grid:
        #     grid.append(line)
        #     if has_no_galaxy(line):
        #         grid.append(line)

        galaxies = []
        for i in range(len(grid)):
            for j, elem in enumerate(grid[i]):
                if elem == "#":
                    galaxies.append((i, j))

        res = 0
        for left, right in combinations(galaxies, 2):
            res += distance(left, right)
        print(res)


def pretty_print(grid: list[list[str]]):
    for line in grid:
        print("".join(line))


def has_no_galaxy(input: list[str]) -> bool:
    return all([i == "." for i in input])


if __name__ == "__main__":
    run()
