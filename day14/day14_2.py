from aocd import get_data
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=500)

def roll_north(platform):
    for k, col in enumerate(platform.T):
        anchor = 0
        rock_count = 0
        for j, space in enumerate(col):
            if space == '#':
                for i in range(anchor, j):
                    if i - anchor < rock_count:
                        platform[i,k] = 'O'
                    else:
                        platform[i,k] = '.'
                rock_count = 0
                anchor = j + 1
            elif space == 'O':
                rock_count += 1
        for i in range(anchor, platform.shape[1]):
            if i - anchor < rock_count:
                platform[i,k] = 'O'
            else:
                platform[i,k] = '.'
    return platform

def roll_west(platform):
    for k, col in enumerate(platform):
        anchor = 0
        rock_count = 0
        for j, space in enumerate(col):
            if space == '#':
                for i in range(anchor, j):
                    if i - anchor < rock_count:
                        platform[k, i] = 'O'
                    else:
                        platform[k, i] = '.'
                rock_count = 0
                anchor = j + 1
            elif space == 'O':
                rock_count += 1
        for i in range(anchor, platform.shape[0]):
            if i - anchor < rock_count:
                platform[k,i] = 'O'
            else:
                platform[k,i] = '.'
    return platform

def roll_south(platform):
    p_flip = np.flip(platform.T, axis=1)
    for k, col in enumerate(p_flip):
        anchor = 0
        rock_count = 0
        for j, space in enumerate(col):
            if space == '#':
                for i in range(anchor, j):
                    if i - anchor < rock_count:
                        p_flip[k, i] = 'O'
                    else:
                        p_flip[k, i] = '.'
                rock_count = 0
                anchor = j + 1
            elif space == 'O':
                rock_count += 1
        for i in range(anchor, platform.shape[1]):
            if i - anchor < rock_count:
                p_flip[k, i] = 'O'
            else:
                p_flip[k, i] = '.'
    platform = np.flip(p_flip, axis=1).T
    return platform

def roll_east(platform):
    p_flip = np.flip(platform, axis=1)
    for k, col in enumerate(p_flip):
        anchor = 0
        rock_count = 0
        for j, space in enumerate(col):
            if space == '#':
                for i in range(anchor, j):
                    if i - anchor < rock_count:
                        p_flip[k, i] = 'O'
                    else:
                        p_flip[k, i] = '.'
                rock_count = 0
                anchor = j + 1
            elif space == 'O':
                rock_count += 1
        for i in range(anchor, platform.shape[0]):
            if i - anchor < rock_count:
                p_flip[k, i] = 'O'
            else:
                p_flip[k, i] = '.'
    platform = np.flip(p_flip, axis=1)

    return platform


def main():
    my_data = get_data(day=14, year=2023)
    lines = my_data.split("\n")
    platform = []
    for line in lines:
        platform.append(np.array(list(line)))
    platform_layouts = []
    found_match = False
    start_val = -1
    cycle_val = -1
    for i in range(1000000000):
        platform = roll_north(platform)
        platform = roll_west(platform)
        platform = roll_south(platform)
        platform = roll_east(platform)
        for j, p in enumerate(platform_layouts):
            if np.array_equal(p, platform):
                start_val = j
                cycle_val = i - j
                found_match = True
                break
        platform_layouts.append(platform.copy())
        if found_match:
            break
    print(start_val)
    print(cycle_val)
    platform_idx = ((999999999 - (start_val)) % (cycle_val))+start_val
    print(platform_idx)
    platform = platform_layouts[platform_idx]

    print(platform)

    # max_load = platform.shape[1]
    total_load = 0
    for i, row in enumerate(platform):
        print(row)
        rock_count = np.count_nonzero(row == 'O')
        print(f'{rock_count} * {platform.shape[1] - i}')
        new_load = rock_count * (platform.shape[1] - i)
        total_load += new_load
    print(total_load)


if __name__ == "__main__":
    main()
