from aocd import get_data

GEAR_DICT = {}

def update_gear(coord, val):
    if coord in GEAR_DICT:
        GEAR_DICT[coord].append(val)
    else:
        GEAR_DICT[coord] = [val]

def check_list(list_of_chars, coords, val):
    for c, coord in zip(list_of_chars, coords):
        if c == "*":
            update_gear(coord, val)

def search_for_chars(lines, line_num, start_idx, end_idx, val):
    vals_to_check = ""
    coords = []
    if line_num > 0:
        start_of_search = max(0, start_idx - 1)
        end_of_search = min(end_idx + 1, len(lines[line_num]) - 1) + 1
        above_line = lines[line_num - 1][start_of_search:end_of_search]
        for i, c in enumerate(above_line):
            coords.append((start_of_search + i, line_num - 1))
        vals_to_check = vals_to_check + above_line
    if line_num < len(lines) - 1:
        start_of_search = max(0, start_idx - 1)
        end_of_search = min(end_idx + 1, len(lines[line_num]) - 1)
        below_line = lines[line_num + 1][start_of_search:end_of_search + 1]
        for i, c in enumerate(below_line):
            coords.append((start_of_search + i, line_num + 1))
        vals_to_check = vals_to_check + below_line
    if start_idx > 0:
        coords.append((start_idx - 1, line_num))
        vals_to_check = vals_to_check + lines[line_num][start_idx - 1]
    if end_idx < len(lines[line_num]) - 1:
        coords.append((end_idx + 1, line_num))
        vals_to_check = vals_to_check + lines[line_num][end_idx + 1]
    check_list(vals_to_check, coords, val)

def main():
    my_data = get_data(day=3, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    print(len(lines))
    sum_of_part_nums = 0
    lines_to_demo = 10
    count = 0
    for i, line in enumerate(lines):
        # print(line)
        curr_str = ""
        start_idx = -1
        end_idx = -1
        found_num = False
        for j, c in enumerate(line):
            if c.isnumeric():
                if not found_num:
                    start_idx = j
                    found_num = True
                end_idx = j
                curr_str += c
            else:
                if found_num:
                    search_for_chars(lines, i, start_idx, end_idx, int(curr_str))
                    curr_str = ""
                    start_idx = -1
                    end_idx = -1
                    found_num = False
        if found_num:
            search_for_chars(lines, i, start_idx, end_idx, int(curr_str))
    for k, v in GEAR_DICT.items():
        if len(v) == 2:
            sum_of_part_nums += v[0] * v[1]
    print(sum_of_part_nums)

if __name__ == "__main__":
    main()
