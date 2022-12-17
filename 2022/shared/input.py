import os

def read_input(day):
    return open(os.path.dirname(os.path.realpath(__file__))+"/../"+day+"/input", encoding="utf-8").read()