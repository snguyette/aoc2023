from aocd import get_data
import re
import itertools

def get_pack_configs(vals, spring_group):
    if sum(vals) + len(vals) - 1 < len(spring_group):

    val_bounds = {}
    start = 0
    for i, val in enumerate(vals):
        val_bounds[i] = {
            'start': start,
            'end': start + val - 1
        }
        start = val_bounds[i]['end'] + 2
    for i in range(0, len(spring_group))

def get_combos(group_data, spring_data):
    for i in range(len(group_data)):
        if i < len(spring_data):
            vals_to_pack = spring_data[:i+1]

def main():
    my_data = get_data(day=12, year=2023)
    lines = my_data.split("\n")
    # print(len(lines))
    total = 0
    lines_to_disp = 0
    # group_counts = []
    # for line in lines:
    #     count = len(line.split(' ')[1].split(','))
    #     group_counts.append(len(line.split(' ')[1].split(',')))
    #     if count > 4:
    #         print(line)
    # print(f'min: {min(group_counts)}, max: {max(group_counts)}')
    # exit()
    for line in lines:
        # print(line)
        line_split = line.split(' ')
        spring_data = line_split[0]
        spring_data = '?'.join([spring_data]*5)
        spring_data = [m for m in re.findall(r'[#?]+', spring_data)]
        # spring_str = '.'.join(spring_data)
        group_data = line_split[1].split(',')
        group_data = [int(val) for val in ','.join([line_split[1]]*5).split(',')]
        # spring_groups = []
        # curr = 0
        # print(spring_data)
        # for c in spring_data:
        #     if c in ['?', '#']:
        #         curr += 1
        #     else:
        #         if curr > 0:
        #             spring_groups.append(curr)
        #             curr = 0
        # if curr > 0:
        #     spring_groups.append(curr)
        # print(spring_data)
        # print(group_data)
        # exit()
        successful_combos = get_combos(group_data, spring_data)
        total += successful_combos
        print(successful_combos)

    print(total)


if __name__ == "__main__":
    main()
