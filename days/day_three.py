import numpy as np

def part_one(input_file):
    rows = __get_rows(input_file)

    gamma_rate = __get_gamma(rows)
    epsilon_rate = __get_epsilon(rows)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def __get_epsilon(rows):
    return __make_binary_str([__get_least_or_most_common_bits(column, least_common=True) for column in rows.T])

def __get_gamma(rows):
    return __make_binary_str([__get_least_or_most_common_bits(column) for column in rows.T])

def __get_least_or_most_common_bits(column, least_common=False):
    one_count = (column == 1).sum()
    zero_count = (column == 0).sum()
    bit = 0 if zero_count > one_count else 1
    if least_common:
        bit = 0 if zero_count <= one_count else 1
    return bit

def part_two(input_file):
    rows = __get_rows(input_file)

    def iteration(position, current_rows, least_or_most_common_bit):
        bit = least_or_most_common_bit(current_rows)[position]
        filtered_rows = current_rows[current_rows.T[position] == int(bit)]
        if(len(filtered_rows) > 1):
            return iteration(position+1, filtered_rows, least_or_most_common_bit)
        else: return filtered_rows[0]

    oxygen_rating = __make_binary_str(iteration(0, rows, __get_gamma))
    co2_scrubber_rating = __make_binary_str(iteration(0, rows, __get_epsilon))
    return int(oxygen_rating, 2) * int(co2_scrubber_rating, 2)

def __make_binary_str(binary_arr):
    return  "".join([str(i) for i in binary_arr])

def __get_rows(file):
    f = open(file, "r")
    rows = [np.array(list(row), dtype=int) for row in f.read().split("\n")[:-1]]
    return np.array(rows)
