def __get_rows(file):
    f = open(file, "r")
    def parse_row(row):
        return [[int(i) for i in point.split(',')] for point in row.replace(' ', '').split('->')]
    rows = [parse_row(row) for row in f.read().split("\n")[:-1]]
    return rows

def draw_line(start, end):
    [x1, y1] = start
    [x2, y2] = end

    if x2==x1 or y1==y2:
        x1, x2 = (x1,x2) if x1<x2 else (x2,x1)
        y1, y2 = (y1,y2) if y1<y2 else (y2,y1)
        line_points = [(i, j) for j in range(y1, y2+1) for i in range(x1,x2+1)]
    else:
        stepX = -1 if x2 < x1 else +1
        stepY = -1 if y2 < y1 else +1
        line_points = [(i, j) for i,j in zip(range(y1, y2+stepY, stepY), range(x1, x2+stepX, stepX))]
    return line_points

def part_one(input_file):
    rows = __get_rows(input_file)
    orthogonals = [element for [a,b] in rows if a[0]==b[0] or a[1]==b[1] for element in draw_line(a,b)]
    filtered = [element for element in orthogonals if orthogonals.count(element) >= 2]
    return len(set(filtered))


def part_two(input_file):
    rows = __get_rows(input_file)
    orthogonals = [element for [a,b] in rows for element in draw_line(a,b)]
    filtered = [element for element in orthogonals if orthogonals.count(element) >= 2]
    return len(set(filtered))