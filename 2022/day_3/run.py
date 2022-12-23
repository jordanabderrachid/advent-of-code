from functools import reduce

from shared.input import read_input

def priority(char):
    offset = 38 if char.isupper() else 96
    return ord(char) - offset

def item_in_common(lines):
    first_group = list(lines[0])
    second_group = list(lines[1])
    third_group = list(lines[2])
    half_size = int(len(second_group)/2)
    first_half, second_half = first_group + second_group[0:half_size], second_group[half_size:] + third_group
    return (set(first_half) & set(second_half)).pop()

def run():
    f = read_input("day_3")
    print(item_in_common(["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]))
    # lines = f.split("\n")
    # priorities = [priority(item_in_common(line)) for line in lines]
    # print(reduce(lambda x,y:x+y, priorities, 0))