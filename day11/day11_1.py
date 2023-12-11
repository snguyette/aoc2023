from aocd import get_data
import numpy as np

def main():
    my_data = get_data(day=11, year=2023)
    map_arr = np.array([list(line) for line in my_data.split("\n")])
    rows = []
    cols = []
    for i, r in enumerate(map_arr):
        if '#' not in r:
            rows.append(i)
    for i, c in enumerate(map_arr.T):
        if '#' not in c:
            cols.append(i)
    galaxy_tuples = list(list(zip(*np.where(map_arr == '#'))))
    galaxy_list = [{'id': i, 'x': val[0], 'y': val[1]} for i, val in enumerate(galaxy_tuples)]
    for galaxy in galaxy_list:
        galaxy['x'] += sum([1 for v in rows if v < galaxy['x']])
        galaxy['y'] += sum([1 for v in cols if v < galaxy['y']])
    total_dist = 0
    for galaxy in galaxy_list:
        for g in galaxy_list:
            if g['id'] > galaxy['id']:
                total_dist += abs(galaxy['x'] - g['x']) + abs(galaxy['y'] - g['y'])
    print(total_dist)

if __name__ == "__main__":
    main()
