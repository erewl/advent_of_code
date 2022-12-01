from days.day_01 import DayOne
from days.day_02 import DayTwo


def main():
    day_number = 2
    days = [
        lambda: DayOne(),
        lambda: DayTwo()
    ]

    day = days[day_number-1]()
    day_str = str(day_number).rjust(2, '0')
    print(day.part_one(f'./input/day_{day_str}.txt'))
    print(day.part_two(f'./input/day_{day_str}.txt'))


if __name__ == '__main__':
    main()