import re


def run():
    with open("input_example.txt") as f:
        lines = f.read().split("\n")
        dug = [(0, 0)]
        for line in lines:
            direction_1, count_1 = parse_line(line)
            direction_2, count_2 = parse_line_part_2(line)
            print(direction_1, count_1, direction_2, count_2)
            # for _ in range(count):
            #     if direction == "R":
            #         dx = 0
            #         dy = 1

            #     if direction == "D":
            #         dx = 1
            #         dy = 0

            #     if direction == "L":
            #         dx = 0
            #         dy = -1

            #     if direction == "U":
            #         dx = -1
            #         dy = 0

            #     x, y = dug[-1]
            #     dug.append((x + dx, y + dy))

        x_min, x_max = 0, 0
        y_min, y_max = 0, 0
        for x, y in dug:
            x_min = min(x_min, x)
            x_max = max(x_max, x)
            y_min = min(y_min, y)
            y_max = max(y_max, y)

        grid = []
        for _ in range(x_max - x_min + 1 + 2):
            grid.append(["." for _ in range(y_max - y_min + 1 + 2)])

        for x, y in dug:
            grid[x - x_min + 1][y - y_min + 1] = "#"

        # for line in grid:
        #     print("".join(line))

        all_locations = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                all_locations.add(str(i) + ":" + str(j))

        grid_x_size = len(grid)
        grid_y_size = len(grid[0])
        visited = set()
        q = [(0, 0)]
        while q:
            x, y = q.pop(0)

            if x < 0 or x >= grid_x_size or y < 0 or y >= grid_y_size:
                continue

            if grid[x][y] != ".":
                continue

            if str(x) + ":" + str(y) in visited:
                continue

            visited.add(str(x) + ":" + str(y))

            q.append([x, y + 1])
            q.append([x, y - 1])
            q.append([x + 1, y])
            q.append([x - 1, y])

        print(len(visited), len(all_locations), len(all_locations) - len(visited))


def parse_line(line: str) -> (str, int):
    pattern = re.compile(r"(R|D|U|L) (\d+)")
    match = pattern.match(line)
    return match.group(1), int(match.group(2))


def parse_line_part_2(line: str) -> (str, int):
    pattern = re.compile(r".*\#(.{5})(\d{1}).*")
    match = pattern.match(line)
    distance = match.group(1)
    direction = int(match.group(2))

    if direction == 0:
        return "R", int(distance, 16)

    if direction == 1:
        return "D", int(distance, 16)

    if direction == 2:
        return "L", int(distance, 16)

    if direction == 3:
        return "U", int(distance, 16)


if __name__ == "__main__":
    run()
