import numpy as np
from collections import Counter
import itertools  

def __get_rows(file):
    f = open(file, "r")
    elements = [int(element) for element in f.read().replace('\n', '').replace(' ', '').split(',')]
    return np.array(elements)

def part_one(input_file):
    fish = __get_rows(input_file)
    fish_count = Counter(fish).items()

    for _ in range(0, 80):
        print(f"Day {i+1}")
        fish_count = [acc for gen, count in fish_count for acc in process_generation(gen, count)]
        # group anglerfish by generation and sum up the counts
        fish_count = [(key, sum(map(value_func, groups))) for key, groups in itertools.groupby(fish_count, key_func)]

    sum_fish = sum([count for _, count in fish_count])
    return sum_fish


def process_generation(gen, count):
    if gen == 0:
        return [(8, count), (6, count)]
    else:
        return [(gen-1, count)]

  
def part_two(input_file):
    fish = __get_rows(input_file)
    fish_count = Counter(fish).items()

    key_func = lambda x: x[0]
    value_func = lambda x: x[1]

    for i in range(1, 257):
        print(f"Day {i}")
        fish_count = [acc for gen, count in fish_count for acc in process_generation(gen, count)]
        # group anglerfish by generation and sum up the counts
        fish_count = [(key, sum(map(value_func, groups))) for key, groups in itertools.groupby(fish_count, key_func)]

    sum_fish = sum([count for _, count in fish_count])
    return sum_fish