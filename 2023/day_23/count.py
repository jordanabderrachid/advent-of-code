def run():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        res = 0
        for line in lines:
            for c in line:
                if c != "#":
                    res += 1
        print(res)
        print(len(lines) * len(lines[0]))


if __name__ == "__main__":
    run()
