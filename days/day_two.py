from functools import reduce


def part_one(input_file):
    instructions = __get_instructions(input_file)
    x, y = reduce(lambda position, instruction: __match_direction(
        instruction, position), instructions, (0, 0))
    return x*y


def part_two(input_file):
    instructions = __get_instructions(input_file)
    x, y, _ = reduce(lambda position, instruction: __match_direction_with_aim(
        instruction, position), instructions, (0, 0, 0))
    return x*y


def __match_direction_with_aim(instruction, position):
    x, y, aim = position
    match instruction:
        case ("forward", length): return (x+length, y + (aim*length), aim)
        case ("down", length): return (x, y, aim+length)
        case ("up", length): return (x, y, aim-length)


def __match_direction(instruction, position):
    x, y = position
    match instruction:
        case ("forward", length): return (x+length, y)
        case ("down", length): return (x, y+length)
        case ("up", length): return (x, y - length)


def __get_instructions(input_file):
    def parse_row(row):
        direction, length = row.split(" ")
        return (direction, int(length))

    f = open(input_file, "r")
    rows = [parse_row(row) for row in f.read().split("\n")[:-1]]
    return rows
