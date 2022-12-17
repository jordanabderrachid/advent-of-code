from functools import reduce

from shared.input import read_input

def sum(lines):
    sums = []
    current = 0
    for line in lines:
        if line == "":
            sums.append(current)
            current = 0        
        else:
            current += int(line)

    return sums

def run():
    f = read_input("day_1")
    lines = f.split("\n")
    sums = sum(lines)
    sums.sort(reverse=True)
    print(reduce(lambda x, y: x+y, sums[0:3]))
