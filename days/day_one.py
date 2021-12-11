
def day_one(inputFile):
    f = open(inputFile, "r")
    rows = f.read().split("\n")
    print(rows)
    print(rows[1:])
    res = [row for idx, row in enumerate(rows[1:], start=1) if int(row) > int(rows[idx-1])]
    print(res)
    return len(res)
        