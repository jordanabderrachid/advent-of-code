import re
from itertools import cycle
import math


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        directions = cycle(list(lines[0]))
        nodes = parse_nodes(lines[2:])

        currents = list(filter(lambda n: ends_with("A", n), list(nodes.keys())))
        steps_arr = []
        for current in currents:
            steps = 0
            while not at_end([current]):
                steps += 1
                direction = next(directions)
                node = nodes[current]
                if direction == "L":
                    current = node[0]
                else:
                    current = node[1]
            steps_arr.append(steps)

        print(lcm_of_list(steps_arr))


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result


def ends_with(letter: str, value: str) -> bool:
    return value.endswith(letter)


def at_end(currents: list[str]) -> bool:
    return all(map(lambda n: ends_with("Z", n), currents))


def parse_nodes(lines):
    pattern = r"(\w+) = \((\w+), (\w+)\)"
    nodes = {}
    for line in lines:
        match = re.match(pattern, line)
        nodes[match.group(1)] = (match.group(2), match.group(3))

    return nodes


if __name__ == "__main__":
    run()
