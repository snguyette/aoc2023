from aocd import get_data
import re
import itertools

# def get_combos(group_data, spring_groups):
#     # print(f'Groups: {group_data}')
#     # print(f'Springs: {spring_groups}')
#     # input()
#     if sum([len(s) for s in spring_groups]) < sum(group_data):
#         return 0
#     if group_data:
#         if spring_groups:
#             curr = group_data[0]
#         else:
#             return 0
#     else:
#         return 1
#     total = 0
#     for i, s in enumerate(spring_groups):
#         windows = len(s) - curr + 1
#         if windows > 2:
#             # print(f'{curr} fits in {s}')
#             new_group_data = [val for j, val in enumerate(group_data) if j > 0]
#             new_spring_groups = [val for j, val in enumerate(spring_groups) if j > i]
#             total += 2 * get_combos(new_group_data, new_spring_groups)
#             for split in get_valid_splits(curr, s):
#                 total += get_combos(new_group_data, [split] + new_spring_groups)
#         elif windows == 2:
#             # print(f'{curr} fits in {s}')
#             valid = sum([1 for v in [s[0], s[-1]] if v == '?'])
#             new_group_data = [val for j, val in enumerate(group_data) if j > 0]
#             new_spring_groups = [val for j, val in enumerate(spring_groups) if j > i]
#             total += valid * get_combos(new_group_data, new_spring_groups)
#         elif windows == 1:
#             new_group_data = [val for j, val in enumerate(group_data) if j > 0]
#             new_spring_groups = [val for j, val in enumerate(spring_groups) if j > i]
#             total += get_combos(new_group_data, new_spring_groups)
#     return total

# def get_valid(idx, size, spring):
#     if '#' not in spring[0:idx]:
#         if idx + size < len(spring):

def get_valid_splits(size, group):
    # diff = len(group) - size
    valid_splits = []
    # print(f'Size: {size}, Group: {group}')
    for i in range(size, len(group) - 2):
        if False not in [val == '?' for val in group[0:i]]:
            if group[i] == '?':
                valid_splits.append(group[i+1:])
    # print(f'Splits: {valid_splits}')
    return valid_splits


def get_combos_new(group_data, spring_groups):
    # if idx >= len(spring_str):
        # return 0
    # print(group_data)
    # print(spring_groups)
    # input()
    if sum([len(s) for s in spring_groups]) < sum(group_data):
        # print('bad')
        return 0
    if group_data:
        if spring_groups:
            curr_group = group_data[0]
            curr_spring = spring_groups[0]
        else:
            # print('bad2')
            return 0
    else:
        if spring_groups:
            if True in ['#' in s for s in spring_groups]:
                # print('bad3')
                return 0
            else:
                # print('no more #')
                return 1
        else:
            # print('both empty')
            return 1
    total = 0
    if '#' not in curr_spring:
        # print('No # in curr_spring')
        if len(curr_spring) < curr_group:
            # print('Group was too large, moving on')
            new_springs = [val for j, val in enumerate(spring_groups) if j > 0]
            return get_combos_new(group_data, new_springs)
        windows = len(curr_spring) - curr_group + 1
        splits = [['?'*(i)] for i in range(windows)]
        for split in splits:
            new_group_data = [val for j, val in enumerate(group_data) if j > 0]
            new_spring_groups = split + [val for j, val in enumerate(spring_groups) if j > 0]
            total += get_combos_new (new_group_data, new_spring_groups)
        # print(f'Found {windows} ways to fit {curr_group}')
        return total
    elif len(curr_spring) < curr_group:
            # print('bad4')
            return 0
    idx = 0
    while curr_spring[idx] != '#':
        if idx >= curr_group:
            # print(f'Found an all ? space to process. Adding {[curr_spring[idx+1:]]} to spring_groups')
            new_groups = [val for j, val in enumerate(group_data) if j > 0]
            new_springs = [curr_spring[idx+1:]] + [val for j, val in enumerate(spring_groups) if j > 0]
            total += get_combos_new(new_groups, new_springs)
        idx += 1
    # print(idx)
    for i in range(max(idx - curr_group, 0), idx + 1):
        # print(f'curr_group: {curr_group}')
        # print(f'i: {i}')
        # print(f'idx: {idx}')
        # print(f'{i+curr_group+2} <= {len(curr_spring)}')
        if i + curr_group + 2 <= len(curr_spring):
            if curr_spring[i+curr_group] == '?':
                # print('Splitting group')
                new_groups = [val for j, val in enumerate(group_data) if j > 0]
                new_springs = [curr_spring[i+curr_group+1:]] + [val for j, val in enumerate(spring_groups) if j > 0]
                total += get_combos_new(new_groups, new_springs)
        else:
            # print('else')
            new_groups = [val for j, val in enumerate(group_data) if j > 0]
            new_springs = [val for j, val in enumerate(spring_groups) if j > 0]
            total += get_combos_new(new_groups, new_springs)
    # print(f'returning {total}\n')
    return total
        
    
    # if not group_data:
    #     if idx < len(spring_str) and '#' not in spring_str[idx:]:
    #         return 1
    #     else:
    #         return 0
    # while spring_str[idx] not in  ['#', '?']:
    #         idx += 1
    # start = idx
    # curr_group = ""
    # while spring_str[idx] in ['#', '?']:
    #     curr_group += spring_str[idx]
    #     idx += 1
    # end = idx

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
        successful_combos = get_combos_new(group_data, spring_data)
        total += successful_combos
        print(successful_combos)
        continue
        u_count = sum([1 for c in spring_data if c == '?'])
        # print(u_count)
        u_possibilities = itertools.product('.#', repeat=u_count)
        successful_combos = []
        for p in u_possibilities:
            # print(p)
            curr = 0
            group_num = 0
            success = True
            u_idx = 0
            for s in spring_data:
                if s == '#':
                    if group_num >= len(group_data):
                        success = False
                        break
                    curr += 1
                elif s == '?':
                    if p[u_idx] == '#':
                        if group_num >= len(group_data):
                            success = False
                            break
                        curr += 1
                    else:
                        if curr > 0:
                            # print(group_data[group_num])
                            # print(curr)
                            if curr != int(group_data[group_num]):
                                success = False
                                # print("mismatch")
                                break
                            curr = 0
                            group_num += 1
                    u_idx += 1
                else:
                    if curr > 0:
                        # print(group_data[group_num])
                        # print(curr)
                        if curr != int(group_data[group_num]):
                            success = False
                            # print("mismatch")
                            break
                        curr = 0
                        group_num += 1
            if group_num < len(group_data):
                if group_num == len(group_data) - 1:
                    if curr != int(group_data[group_num]):
                        success = False
                else:
                    success = False
            if success:
                # print(f"{p}: success")
                total += 1
                successful_combos.append(p)
            # else:
            #     print("fail")
        # break
        # print(group_data)
        # print(spring_data)
        # for c in successful_combos:
        #     new_str = ""
        #     idx = 0
        #     for s in spring_data:
        #         if s == '?':
        #             new_str += c[idx]
        #             idx += 1
        #         else:
        #             new_str += s
        #     print(new_str)
        # if lines_to_disp == 0:
        #     break
        # else:
        #     lines_to_disp -= 1

    print(total)


if __name__ == "__main__":
    main()
