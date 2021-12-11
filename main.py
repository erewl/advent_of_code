from days.day_one import *
from days.day_two import part_one

def execute(inputPath, day_func):
    print(day_func(inputPath))

input_path = 'input'
test_input_path = 'test_input'

execute(f"{input_path}/02_01.txt", part_one)
