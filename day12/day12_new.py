from aocd import get_data
import re
import itertools
import logging

# def get_pack_configs(vals, spring_group):
#     if sum(vals) + len(vals) - 1 < len(spring_group):

#     val_bounds = {}
#     start = 0
#     for i, val in enumerate(vals):
#         val_bounds[i] = {
#             'start': start,
#             'end': start + val - 1
#         }
#         start = val_bounds[i]['end'] + 2
#     for i in range(0, len(spring_group))

# def get_combos(group_data, spring_data):
#     for i in range(len(group_data)):
#         if i < len(spring_data):
#             vals_to_pack = spring_data[:i+1]

def pack_configs(group_data, spring_group):
    curr = group_data[0]
    if len(group_data) > 1:
        min_rem = sum(group_data[1:])+len(group_data)-1
        if min_rem + curr > len(spring_group):
            return 0
        total = 0
        min = 0
        max = (len(spring_group) - min_rem - curr) + 1
        for i in range(min, max):
            if '#' not in spring_group[:i] and spring_group[i+curr] != '#':
                total += pack_configs(group_data[1:], spring_group[i+curr+1:])
        logging.debug(f'{total} ways to pack group data into spring group')
        return total
    else:
        if curr > len(spring_group):
            return 0
        total = 0
        min = 0
        max = len(spring_group) - curr + 1
        for i in range(min, max):
            if '#' not in spring_group[:i] and '#' not in spring_group[i+curr+1:]:
                total += 1
        logging.debug(f'{total} ways to pack group data into spring group')
        return total

def get_combos(group_data, spring_groups, count, curr_group_distro):
    total = 0
    logging.debug(group_data)
    logging.debug(spring_groups)
    logging.debug(count)
    logging.debug(curr_group_distro)
    s = spring_groups[0]
    if len(spring_groups) > 1:
        if '#' in s:
            logging.debug('# in s')
            if count > 0:
                count -= 1
            min = 1
            max = len(group_data) - count + 1
        else:
            logging.debug('no # in s')
            min = 0
            max = max = len(group_data) - count + 1
        for i in range(min, max):
            new_distro = curr_group_distro.copy()
            new_distro.append(i)
            if i == 0:
                total += get_combos(group_data, spring_groups[1:], count, curr_group_distro)
            else:
                num_configs = pack_configs(group_data[:i], s)
                if num_configs:
                    # combos = get_combos(group_data[i:], spring_groups[1:], count)
                    total += num_configs * get_combos(group_data[i:], spring_groups[1:], count, curr_group_distro)
        logging.debug(f'returning {total}')
        return total
    else:
        if '#' in s:
            logging.debug('# in s')
            if group_data:
                logging.debug('group data exists')
                return pack_configs(group_data, s)
            else:
                logging.debug('no group data')
                return 0
        else:
            logging.debug('no # in s')
            if group_data:
                logging.debug('group data exists')
                return pack_configs(group_data, s)
            else:
                logging.debug('no group data')
                return 1


def main():
    logging.basicConfig(level=logging.DEBUG)
    my_data = get_data(day=12, year=2023)
    lines = my_data.split("\n")
    total = 0
    lines_to_disp = 0
    for line in lines:
        # print(line)
        line_split = line.split(' ')
        spring_data = line_split[0]
        spring_data = '?'.join([spring_data]*5)
        spring_data = [m for m in re.findall(r'[#?]+', spring_data)]
        count = sum([1 for s in spring_data if '#' in s])
        # spring_str = '.'.join(spring_data)
        group_data = line_split[1].split(',')
        group_data = [int(val) for val in ','.join([line_split[1]]*5).split(',')]
        curr_group_distro = []
        successful_combos = get_combos(group_data, spring_data, count, curr_group_distro)
        total += successful_combos
        print(successful_combos)
        input()

    print(total)


if __name__ == "__main__":
    main()
