from aocd import get_data
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=500)

def main():
    my_data = get_data(day=18, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    directions = []
    steps = []
    hex_vals = []
    for line in lines:
        data = line.split(' ')
        directions.append(data[0])
        steps.append(int(data[1]))
        hex_vals.append(data[2])
    x = 0
    y = 0
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for d, s in zip(directions, steps):
        if d == 'U':
            x -= s
        elif d == 'L':
            y -= s
        elif d == 'R':
            y += s
        elif d == 'D':
            x += s
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    print(f'X range: {min_x}, {max_x}')
    print(f'Y range: {min_y}, {max_y}')
    x_range = max_x - min_x
    y_range = max_y - min_y
    x = -min_x
    y = -min_y
    dig_grid = np.full((x_range+1, y_range+1), '.')
    # print(dig_grid)
    for d, s in zip(directions, steps):
        for i in range(s):
            if d == 'U':
                x -= 1
                dig_grid[x, y] = '#'
            elif d == 'L':
                y -= 1
                dig_grid[x, y] = '#'
            elif d == 'R':
                y += 1
                dig_grid[x, y] = '#'
            elif d == 'D':
                x += 1
                dig_grid[x, y] = '#'
    total = np.count_nonzero(dig_grid == '#')
    for i, r in enumerate(dig_grid):
        if i in [0, dig_grid.shape[0]-1]:
            continue
        state = 'o'
        inside_line = False
        line_start = None
        for j, c in enumerate(r):
            if j == dig_grid.shape[1]-1:
                continue
            if c == '#':
                if dig_grid[i, j+1] == '#':
                    if not inside_line:
                        if dig_grid[i-1, j] == '#':
                            line_start = 'u'
                            inside_line = True
                        else:
                            line_start = 'd'
                            inside_line = True
                    else:
                        continue
                else:
                    if inside_line:
                        if dig_grid[i-1, j] == '#':
                            if line_start == 'd':
                                if state == 'i':
                                    state = 'o'
                                else:
                                    state = 'i'
                            inside_line = False
                            line_start = None
                        else:
                            if line_start == 'u':
                                if state == 'i':
                                    state = 'o'
                                else:
                                    state = 'i'
                            inside_line = False
                            line_start = None
                    else:
                        if state == 'i':
                            state = 'o'
                        else:
                            state = 'i'
            else:
                if state == 'i':
                    total += 1
    print(total)
    # print(dig_grid)
    # for r in dig_grid:
        # print(r)
    # print(dig_grid)
    # print(len(lines))

if __name__ == "__main__":
    main()
