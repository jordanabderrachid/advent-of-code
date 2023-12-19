# from itertools import combinations_with_replacement
import re
from functools import cache


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")

        res = 0
        for line in lines:
            input, spec = line.split(" ")
            spec = tuple(map(int, spec.split(",")))
            input = "?".join([input] * 5)
            spec = spec * 5
            print(input, spec)
            res += count(input, spec)
            # res += search(input, spec)

        print(res)


@cache
def count(input: str, spec: tuple) -> int:
    if input == "":
        return 1 if spec == () else 0

    if spec == ():
        return 0 if "#" in input else 1

    result = 0
    if input[0] == ".":
        result += count(input[1:], spec)

    if input[0] == "#":
        if (
            spec[0] <= len(input)
            and "." not in input[: spec[0]]
            and (spec[0] == len(input) or input[spec[0]] != "#")
        ):
            result += count(input[spec[0] + 1 :], spec[1:])
        else:
            result += 0

    if input[0] == "?":
        # case were ? is subs with .
        result += count(input[1:], spec)

        # case where ? is subs with #
        if (
            spec[0] <= len(input)
            and "." not in input[: spec[0]]
            and (spec[0] == len(input) or input[spec[0]] != "#")
        ):
            result += count(input[spec[0] + 1 :], spec[1:])
        else:
            result += 0

    return result


def search(input: str, spec: str) -> int:
    slots = count_slots(input)
    print(slots)
    res = [0]

    # search_space = 2**slots
    attempt = [0]

    def backtrack(curr: list[str]):
        if len(curr) == slots:
            attempt[0] += 1
            if match(replace(input, curr), spec):
                res[-1] += 1
            return

        if not match(replace(input, curr), spec, partial=True):
            return

        backtrack(curr + ["."])
        backtrack(curr + ["#"])

    backtrack(["."])
    backtrack(["#"])

    # print(attempt[0], "/", search_space)
    return res[-1]


def replace(input: str, arrangement: list[str]) -> str:
    out = input
    for c in arrangement:
        out = out.replace("?", c, 1)
    return out


def match(input: str, spec: str, partial=False) -> bool:
    # print(input, spec, partial)
    spec = [int(v) for v in spec.split(",")]
    pattern = re.compile(r"\#+")

    if partial:
        input = input[: input.find("?")]

    actuals = []
    for match in pattern.finditer(input):
        actuals.append(len(match.group()))

    if partial:
        mismatch = 0
        for actual, expected in zip(actuals, spec):
            if actual > expected:
                return False

            if actual != expected:
                mismatch += 1

        return mismatch <= 1

    return actuals == spec


def count_slots(input: str) -> int:
    res = 0
    for c in list(input):
        if c == "?":
            res += 1
    return res


if __name__ == "__main__":
    run()
