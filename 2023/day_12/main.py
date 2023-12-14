# from itertools import combinations_with_replacement
import re


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")

        res = 0
        for line in lines:
            input, spec = line.split(" ")
            for candidate in generate_arrangement(count_slots(input)):
                if match(replace(input, candidate), spec):
                    res += 1

        print(res)


def replace(input: str, arrangement: list[str]) -> str:
    out = input
    for c in arrangement:
        out = out.replace("?", c, 1)
    return out


def match(input: str, spec: str) -> bool:
    # print(input, spec)
    spec = [int(v) for v in spec.split(",")]
    pattern = re.compile(r"\#+")

    actuals = []
    for match in pattern.finditer(input):
        actuals.append(len(match.group()))

    return actuals == spec


def count_slots(input: str) -> int:
    res = 0
    for c in list(input):
        if c == "?":
            res += 1
    return res


def generate_arrangement(slot_count: int) -> list[list[str]]:
    res = []

    def backtrack(curr: list[str]):
        if len(curr) == slot_count:
            res.append(curr)
            return

        backtrack(curr + ["."])
        backtrack(curr + ["#"])

    backtrack(["."])
    backtrack(["#"])

    return res


if __name__ == "__main__":
    run()
