import re

from shared.input import read_input

class Range:
    def __init__(self, start, end) -> None:
        if start > end:
            raise ValueError("start={} greater than end={}".format(start, end))
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start + 1

    def overlaps_with(self, other: "Range") -> bool:
        l = set(range(self.start, self.end+1))
        r = set(range(other.start, other.end+1))
        return len(l & r) > 0

matcher = re.compile("^(\d+)-(\d+),(\d+)-(\d+)$")

def parse(line):
    result = matcher.search(line)
    a,b,c,d = result.groups()
    return (Range(int(a),int(b)), Range(int(c),int(d)))

def run():
    f = read_input("day_4")
    lines = f.split("\n")
    overlap_count = 0
    for line in lines[:-1]:
        l, r = parse(line)
        if l.overlaps_with(r):
            overlap_count += 1

    print(overlap_count)
