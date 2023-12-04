def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")

        copies_counts = {}
        for i in range(len(lines)):
            copies_counts[i + 1] = 1
        print(copies_counts)

        for i, line in enumerate(lines):
            game_number = i + 1
            match_count = points(line)
            for j in range(1, match_count + 1):
                if game_number + j <= len(lines):
                    copies_counts[game_number + j] += copies_counts[game_number]

        print(sum([v for _, v in copies_counts.items()]))


def points(line: str) -> int:
    _, numbers_part = line.split(":")
    expected_part, actual_part = numbers_part.split("|")
    expected_part = expected_part.strip()
    actual_part = actual_part.strip()
    expected_set = set()
    for d in expected_part.split(" "):
        if d != "":
            expected_set.add(int(d))

    actual_set = set()
    for d in actual_part.split(" "):
        if d != "":
            actual_set.add(int(d))

    intersection = expected_set.intersection(actual_set)
    return len(intersection)


if __name__ == "__main__":
    run()
