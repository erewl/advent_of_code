import days.day_seven as d


def execute(inputPath, day_func):
    print(day_func(inputPath))


input_path = 'input'
test_input_path = 'test_input'

input_file = "07.txt"

execute(f"{input_path}/{input_file}", d.part_one)
# execute(f"{input_path}/{input_file}", d.part_two)
