from days.day_01 import DayOne


def main():
    day = DayOne()
    day_number = '01'
    print(day.part_one(f'./input/day_{day_number}.txt'))
    print(day.part_two(f'./input/day_{day_number}.txt'))


if __name__ == '__main__':
    main()