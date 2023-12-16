def run():
    with open("input.txt") as f:
        input = f.read()
        boxes = [[]] * 255

        for s in input.split(","):
            if "-" in s:
                key = s.split("-")[0]
                boxes[hash(key)] = remove(key, boxes[hash(key)])

            if "=" in s:
                key, value = s.split("=")
                boxes[hash(key)] = set(key, int(value), boxes[hash(key)])

        res = 0
        for i in range(len(boxes)):
            for j in range(len(boxes[i])):
                res += (i + 1) * (j + 1) * boxes[i][j][1]
        print(res)


def hash(input: str) -> int:
    res = 0
    for c in input:
        res += ord(c)
        res *= 17
        res = res % 256
    return res


def set(key, value, box):
    for i in range(len(box)):
        if key == box[i][0]:
            box[i] = (key, value)
            return box

    return box + [(key, value)]


def remove(key, box):
    index = -1
    for i in range(len(box)):
        if box[i][0] == key:
            index = i
            break

    if index == -1:
        return box

    return box[:i] + box[i + 1 :]


if __name__ == "__main__":
    run()
