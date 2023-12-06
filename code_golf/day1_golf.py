from aocd import get_data
import re
total1, total2 = 0, 0
num_regex = r'(?=(1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine|zero))'
NUM_WORDS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9}
for line in get_data(day=1, year=2023).split("\n"):
    nums = [c for c in line if c.isnumeric()]
    total1 += int(f'{nums[0]}{nums[-1]}')
    nums = [m for m in re.findall(num_regex, line)]
    for i, num in enumerate(nums): nums[i] = int(num) if num.isnumeric() else NUM_WORDS[num]
    total2 += int(f'{nums[0]}{nums[-1]}')
print(f'Part 1: {total1}, Part 2: {total2}')