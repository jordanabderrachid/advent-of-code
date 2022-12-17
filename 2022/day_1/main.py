import os
from functools import reduce

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

def main():
    f = open(os.path.dirname(os.path.realpath(__file__))+"/input", encoding="utf-8").read()
    lines = f.split("\n")
    sums = sum(lines)
    sums.sort(reverse=True)
    print(reduce(lambda x, y: x+y, sums[0:3]))

if __name__ == "__main__":
    main()