import numpy as np

def __get_rows(file):
    f = open(file, "r")
    elements = [int(element) for element in f.read().replace('\n', '').replace(' ', '').split(',')]
    return elements


def part_one(input_file):
    rows = np.array(__get_rows(input_file))
    middle = int(np.median(rows))
    fuel_needed = np.abs(rows - middle)
    return sum(fuel_needed)

def part_two(input_file):
    rows = __get_rows(input_file)

    return 0