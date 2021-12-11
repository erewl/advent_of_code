
def day_one(inputFile):
    f = open(inputFile, "r")
    rows = f.read().split("\n")[:-1]
    res = [row for idx, row in enumerate(rows[1:], start=1) if int(row) > int(rows[idx-1])]
    return len(res)

def day_one_2(input_file):
    f = open(input_file, "r")
    rows = [int(s) for s  in f.read().split("\n")[:-1]]
    sums = [sum(rows[i:i+3]) for i in range(0, len(rows)-2)]
    res = [row for idx, row in enumerate(sums[1:], start=1) if int(row) > int(sums[idx-1])]
    return len(res)