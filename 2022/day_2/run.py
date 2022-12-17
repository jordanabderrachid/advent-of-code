from functools import reduce

from shared.input import read_input

def score_choice(them, us):
    match them:
        case "A":
            if us == "X":   # C
                return 3
            elif us == "Y": # A
                return 1
            else:           # B  
                return 2
        case "B":
            if us == "X":   # A
                return 1
            elif us == "Y": # B
                return 2
            else:           # C
                return 3

        case "C":
            if us == "X":   # B
                return 2
            elif us == "Y": # C
                return 3
            else:           # A
                return 1

    return 0

def score_outcome(us):
    match us:
        case "X":
            return 0
        case "Y":
            return 3
        case "Z":
            return 6
        case _:
            return 0

def score(line):
    choices = line.split(" ")
    them, us = choices[0], choices[1]
    return score_choice(them, us) + score_outcome(us)

def run():
    f = read_input("day_2")
    lines = f.split("\n")
    scores = [score(line) for line in lines]
    print(reduce(lambda x,y:x+y, scores, 0))
