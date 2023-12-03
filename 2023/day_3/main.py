import re


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")

        numbers_dict = {}
        for v, coord in find_numbers(lines):
            d = int(v)
            x, y = coord
            for s in range(len(str(v))):
                numbers_dict[(x, y + s)] = d
        res = 0
        for coord in find_stars(lines):
            gears = set()
            ratio = 1
            for x, y in neighbors_coords(coord[0], coord[1]):
                if (x, y) in numbers_dict:
                    gears.add(numbers_dict[(x, y)])

            if len(gears) > 1:
                for g in gears:
                    ratio = ratio * g
                print(gears, ratio)
                res += ratio

        print(res)


def find_numbers(lines: list[str]) -> list[tuple[str, tuple[int, int]]]:
    res = []
    for i in range(len(lines)):
        line = lines[i]
        for m in re.finditer("\d+", line):
            res.append((m.group(0), (i, m.start(0))))

    return res


def find_stars(lines: list[str]) -> list[tuple[int, int]]:
    res = []
    for i in range(len(lines)):
        line = lines[i]
        for m in re.finditer("\*", line):
            res.append((i, m.start(0)))

    return res


def neighbors_coords(x: int, y: int) -> list[tuple[int, int]]:
    res = []
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        res.append((x + i, y + j))

    return res


if __name__ == "__main__":
    run()
