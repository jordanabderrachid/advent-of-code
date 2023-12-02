from collections import defaultdict
import re


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        s = 0
        for line in lines:
            s += parse_game(line)
        print(s)


# LIMITS = {"red": 12, "green": 13, "blue": 14}


def parse_game(line: str) -> int:
    game_id_matcher = re.match("^Game (\d+)\:", line)

    cubes = defaultdict(lambda: 0)
    rest = line[game_id_matcher.end() :]
    for game_set in rest.split(";"):
        for draw in game_set.split(","):
            count, color = draw.strip().split(" ")
            cubes[color] = max(cubes[color], int(count))

    power = 1
    for v in cubes.values():
        power *= v

    return power


if __name__ == "__main__":
    run()
