import numpy as np
from collections import Counter
import itertools  

key_func = lambda x: x[0]
value_func = lambda x: x[1]

def __get_rows(file):
    f = open(file, "r")
    elements = [int(element) for element in f.read().replace('\n', '').replace(' ', '').split(',')]
    return np.array(elements)

def part_one(input_file):
    fish = __get_rows(input_file)
    generations = Counter(fish).items()

    for i in range(0, 80):
        print(f"Day {i+1}")
        generations = [acc for gen, count in generations for acc in process_generation(gen, count)]
        # group anglerfish by generation and sum up the counts
        generations = [(key, sum(map(value_func, groups))) for key, groups in itertools.groupby(generations, key_func)]

    sum_fish = sum([count for _, count in generations])
    return sum_fish


def process_generation(gen, count):
    if gen == 0:
        return [(8, count), (6, count)]
    else:
        return [(gen-1, count)]

  
def part_two(input_file):
    fish = __get_rows(input_file)
    generations = Counter(fish).items()

    for i in range(0, 256):
        print(f"Day {i+1}")
        generations = [new_gen for gen, count in generations for new_gen in process_generation(gen, count)]
        # group anglerfish by generation and sum up the counts
        generations = [(key, sum(map(value_func, groups))) for key, groups in itertools.groupby(generations, key_func)]

    sum_fish = sum([count for _, count in generations])
    return sum_fish