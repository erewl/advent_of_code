import days.day_two as d


def execute(inputPath, day_func):
    print(day_func(inputPath))


input_path = 'input'
test_input_path = 'test_input'

execute(f"{input_path}/02_01.txt", d.part_one)
execute(f"{input_path}/02_01.txt", d.part_two)
