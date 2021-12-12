import numpy as np

def part_one(input_file):
    rows = __get_rows(input_file)
    gamma_rate = "".join([ str(np.bincount(r).argmax()) for r in rows.T])

    inversion_table = {ord('0'): '1', ord('1'): '0'} 
    epsilon_rate = gamma_rate.translate(inversion_table)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def __get_rows(file):
    f = open(file, "r")
    rows = [np.array(list(row), dtype=int) for row in f.read().split("\n")[:-1]]
    return np.array(rows)
