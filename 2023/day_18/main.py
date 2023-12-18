import re


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        coords = [(0, 0)]
        boundary_points = 0
        for line in lines:
            direction, count = parse_line_part_2(line)
            boundary_points += count
            x, y = coords[-1]
            if direction == "R":
                dx = 0
                dy = count

            if direction == "D":
                dx = count
                dy = 0

            if direction == "L":
                dx = 0
                dy = -count

            if direction == "U":
                dx = -count
                dy = 0

            coords.append((x + dx, y + dy))

        # this is the shoelace formula
        # https://en.wikipedia.org/wiki/Shoelace_formula
        A = (
            abs(
                sum(
                    [
                        coords[i][0]
                        * (coords[(i + 1) % len(coords)][1] - coords[i - 1][1])
                        for i in range(len(coords))
                    ]
                )
            )
            // 2
        )

        # this is the pick's theorem
        # https://en.wikipedia.org/wiki/Pick%27s_theorem
        inside_points = A - boundary_points // 2 + 1
        print(boundary_points + inside_points)


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
