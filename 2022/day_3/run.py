from functools import reduce

from shared.input import read_input

def priority(char):
    offset = 38 if char.isupper() else 96
    return ord(char) - offset

def item_in_common(lines):
    first_group = list(lines[0])
    second_group = list(lines[1])
    third_group = list(lines[2])
    return (set(first_group) & set(second_group) & set(third_group)).pop()

def run():
    f = read_input("day_3")
    # print(item_in_common(["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]))
    lines = f.split("\n")
    priorities = []
    for i in range(0, int(len(lines)/3)):
        priorities.append(priority(item_in_common(lines[3*i:3*i+3])))
    print(reduce(lambda x,y:x+y, priorities, 0))
