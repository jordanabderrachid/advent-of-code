def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        s = 0
        for line in lines:
            d = extract_digits(line)
            s += int(DIGITS[d[0]] * 10 + DIGITS[d[-1]])
        print(s)


DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def extract_digits(line: str) -> list[str]:
    first_candidates = []
    last_candidates = []
    for digit_str in DIGITS.keys():
        lowest_index = line.find(digit_str)
        if lowest_index != -1:
            first_candidates.append((lowest_index, digit_str))

        highest_index = line.rfind(digit_str)
        if lowest_index != -1:
            last_candidates.append((highest_index, digit_str))

    first_candidates.sort(key=lambda c: c[0])
    last_candidates.sort(key=lambda c: c[0], reverse=True)

    return [first_candidates[0][1], last_candidates[0][1]]


if __name__ == "__main__":
    run()
