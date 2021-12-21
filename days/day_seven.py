import numpy as np
import math

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
    rows = np.array(__get_rows(input_file))
    middle = int(np.median(rows))

    def get_needed_fuel(crab_positions, optimal_position):
        steps_needed = np.abs(crab_positions - optimal_position)
        fuel_needed = [sum(range(1, step+1)) for step in steps_needed]
        print(optimal_position, sum(fuel_needed))
        return sum(fuel_needed)

    minmax = 167
    fuel = np.min([get_needed_fuel(rows, pos) for pos in range(middle-minmax, middle+minmax)])
    return fuel
