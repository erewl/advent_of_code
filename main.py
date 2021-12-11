from days.day_one import *

def execute(inputPath, day_func):
    print(day_func(inputPath))

input_path = 'input'
test_input_path = 'test_input'
execute(f"{input_path}/01_01.txt", day_one_2)
