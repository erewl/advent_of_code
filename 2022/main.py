from days.day_01 import DayOne
from days.day_02 import DayTwo
from days.day_03 import DayThree
from days.day_04 import DayFour
from days.day_05 import DayFive
from days.day_06 import DaySix
from days.day_08 import DayEight


def main():
    day_number = 8
    days = [
        DayOne(),
        DayTwo(),
        DayThree(),
        DayFour(),
        DayFive(),
        DaySix(),
        (),
        DayEight()
    ]

    day = days[day_number-1]
    day_str = str(day_number).rjust(2, '0')

    print(f'Day {day_number}')
    print(f"Part 1: {day.part_one(f'./input/day_{day_str}.txt')}")
    print(f"Part 2: {day.part_two(f'./input/day_{day_str}.txt')}")


if __name__ == '__main__':
    main()