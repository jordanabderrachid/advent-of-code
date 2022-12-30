import re

from shared.input import read_input

# [P]     [C]         [M]            
# [D]     [P] [B]     [V] [S]        
# [Q] [V] [R] [V]     [G] [B]        
# [R] [W] [G] [J]     [T] [M]     [V]
# [V] [Q] [Q] [F] [C] [N] [V]     [W]
# [B] [Z] [Z] [H] [L] [P] [L] [J] [N]
# [H] [D] [L] [D] [W] [R] [R] [P] [C]
# [F] [L] [H] [R] [Z] [J] [J] [D] [D]
#  1   2   3   4   5   6   7   8   9 
stacks = [
    list(["F", "H", "B", "V", "R", "Q", "D", "P"]),
    list(["L", "D", "Z", "Q", "V", "W"]),
    list(["H", "L", "Z", "Q", "G", "R", "P", "C"]),
    list(["R", "D", "H", "F", "J", "V", "B"]),
    list(["Z", "W", "L", "C"]),
    list(["J", "R", "P", "N", "T", "G", "V", "M"]),
    list(["J", "R", "L", "V", "M", "B", "S"]),
    list(["D", "P", "J"]),
    list(["D", "C", "N", "W", "V"]),
]


matcher = re.compile("^move (\d+) from (\d+) to (\d+)$")

def parse(line):
    result = matcher.search(line)
    if result is None:
        return (0,0,0)

    n, f, t = result.groups()
    return (int(n), int(f)-1, int(t)-1)

def run():
    f = read_input("day_5")
    lines = f.split("\n")
    for line in lines:
        n,f,t = parse(line)
        buf = list()
        for _ in range(n):
            buf.append(stacks[f].pop())
        for _ in range(n):
            stacks[t].append(buf.pop())

    for stack in stacks:
        print(stack.pop())
