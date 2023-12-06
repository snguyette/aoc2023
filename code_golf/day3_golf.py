from aocd import get_data; import numpy as np; import re; sum_of_part_nums = 0
GEAR_DICT = {}; lines = get_data(day=3, year=2023).split("\n")
char_array = np.array([list(line) for line in lines], dtype=str)
for i, row in enumerate(char_array):
    for num in [m for m in re.finditer(r'\d+', lines[i])]:
        section_to_check = char_array[max(i - 1, 0):min(i + 1, len(lines) - 1) + 1,
            max(num.start(0) - 1, 0):min(num.end(0) + 1, len(lines[i]))].flatten()
        if True in [(not c.isnumeric() and c != '.') for c in section_to_check]:
            sum_of_part_nums += int(num[0])
        for j in range(max(i - 1, 0), min(i + 1, len(lines) - 1) + 1):
            for k in range(max(num.start(0) - 1, 0), min(num.end(0) + 1, len(lines[i]))):
                if char_array[j, k] == '*':
                    if (j, k) in GEAR_DICT: GEAR_DICT[(j, k)].append(int(num[0]))
                    else: GEAR_DICT[(j, k)] = [int(num[0])]
sum_of_gears = sum([v[0] * v[1] if len(v) == 2 else 0 for k, v in GEAR_DICT.items()])
print(f'Part 1: {sum_of_part_nums}, Part 2: {sum_of_gears}')