
def day_one(input_file):
    rows = __get_rows(input_file)
    return len(__filter_for_increasing_rows(rows))

def __get_rows(file):
    f = open(file, "r")
    rows_as_int = [int(row) for row in f.read().split("\n")[:-1]]
    return rows_as_int

def __filter_for_increasing_rows(rows):
    return [row for idx, row in enumerate(rows[1:], start=1) if row > rows[idx-1]]

def day_one_2(input_file):
    rows = __get_rows(input_file)
    sums = [sum(rows[i:i+3]) for i in range(0, len(rows)-2)]
    return len(__filter_for_increasing_rows(sums))
