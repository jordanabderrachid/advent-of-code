def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        res = 0
        for line in lines:
            res += extrapolate_left([int(v) for v in line.split(" ")])
        print(res)


def extrapolate(input: list[int]) -> int:
    values = [input]
    while not all_zeros(values[-1]):
        current_values = values[-1]
        differences = []
        for i in range(len(current_values) - 1):
            differences.append(current_values[i + 1] - current_values[i])
        values.append(differences)

    res = 0
    for i in range(len(values) - 1, -1, -1):
        res += values[i][-1]

    return res


def extrapolate_left(input: list[int]) -> int:
    values = [input]
    while not all_zeros(values[-1]):
        current_values = values[-1]
        differences = []
        for i in range(len(current_values) - 1):
            differences.append(current_values[i + 1] - current_values[i])
        values.append(differences)

    res = 0
    for i in range(len(values) - 1, -1, -1):
        res = values[i][0] - res

    return res


def all_zeros(values: list[int]) -> bool:
    return all([v == 0 for v in values])


if __name__ == "__main__":
    run()
    # print(extrapolate_left([10, 13, 16, 21, 30, 45]))
