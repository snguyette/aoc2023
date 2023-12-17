from aocd import get_data

def check_list(list_of_chars):
    for c in list_of_chars:
        if not c.isnumeric() and c != ".":
            return True
    return False

def search_for_chars(lines, line_num, start_idx, end_idx):
    vals_to_check = ""
    if line_num > 0:
        above_line = lines[line_num - 1]
        vals_to_check = vals_to_check + above_line[max(0, start_idx - 1):min(end_idx + 1, len(above_line) - 1) + 1]
    if line_num < len(lines) - 1:
        below_line = lines[line_num + 1]
        start_of_search = max(0, start_idx - 1)
        end_of_search = min(end_idx + 1, len(below_line) - 1)
        vals_to_check = vals_to_check + below_line[start_of_search:end_of_search + 1]
    if start_idx > 0:
        vals_to_check = vals_to_check + lines[line_num][start_idx - 1]
    if end_idx < len(lines[line_num]) - 1:
        vals_to_check = vals_to_check + lines[line_num][end_idx + 1]
    return check_list(vals_to_check)

def main():
    my_data = get_data(day=3, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    print(len(lines))
    sum_of_part_nums = 0
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
                    if search_for_chars(lines, i, start_idx, end_idx):
                        sum_of_part_nums += int(curr_str)
                    curr_str = ""
                    start_idx = -1
                    end_idx = -1
                    found_num = False
        if found_num:
            if search_for_chars(lines, i, start_idx, end_idx):
                sum_of_part_nums += int(curr_str)
    print(sum_of_part_nums)

if __name__ == "__main__":
    main()
