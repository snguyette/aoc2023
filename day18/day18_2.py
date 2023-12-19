from aocd import get_data
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=500)

DIR_CONV = ['R', 'D', 'L', 'U']

CLOCKWISE = ['RD', 'DL', 'LU', 'UR']

def main():
    my_data = get_data(day=18, year=2023)
    # print(my_data)
    # my_data = "R 6 (#70c710)\nD 5 (#0dc571)\nL 2 (#5713f0)\nD 2 (#d2c081)\nR 2 (#59c680)\nD 2 (#411b91)\nL 5 (#8ceee2)\nU 2 (#caa173)\nL 1 (#1b58a2)\nU 2 (#caa171)\nR 2 (#7807d2)\nU 3 (#a77fa3)\nL 2 (#015232)\nU 2 (#7a21e3)"
    lines = my_data.split("\n")
    directions = []
    steps = []
    # hex_vals = []
    bends = []
    prev = None
    for line in lines:
        hex_val = line.split('#')[1][:-1]
        direction = DIR_CONV[int(hex_val[-1])]
        directions.append(direction)
        steps.append(int(hex_val[:-1], 16))
        if prev:
            bends.append(f'{prev}{direction}')
        else:
            first_dir = direction
        prev = direction
    bends = [f'{prev}{first_dir}'] + bends
    x = 0
    y = 0
    coord_list = [(x, y)]
    for i, (d, s) in enumerate(zip(directions, steps)):
        idx = i+1
        if idx == len(directions):
            idx = 0
        if bends[i] in CLOCKWISE and bends[idx] in CLOCKWISE:
            s += 1
        elif bends[i] not in CLOCKWISE and bends[idx] not in CLOCKWISE:
            s -= 1
        if d == 'U':
            y += s
        elif d == 'L':
            x -= s
        elif d == 'R':
            x += s
        elif d == 'D':
            y -= s
        coord_list.append((x, y))
    area = 0
    for i, coord in enumerate(coord_list[:-1]):
        next_coord = coord_list[i+1]
        area += (coord[0]*next_coord[1] - next_coord[0]*coord[1])
    area = abs(area / 2)
    print(area)

if __name__ == "__main__":
    main()
