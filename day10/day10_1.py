from aocd import get_data; import numpy as np

def main():
    my_data = get_data(day=10, year=2023)
    map_arr = np.array([list(line) for line in my_data.split("\n")])
    start_coord = list(list(zip(*np.where(map_arr == 'S')))[0])

    step = 0
    if map_arr[start_coord[0] - 1][start_coord[1]] in ['7', 'F', '|']:
        step += 1
        start_coord[0] -= 1
        prev = 'u'
    elif map_arr[start_coord[0]][start_coord[1] - 1] in ['L', 'F', '-']:
        step += 1
        start_coord[1] -= 1
        prev = 'l'
    elif map_arr[start_coord[0]][start_coord[1] + 1] in ['7', 'J', '-']:
        step += 1
        start_coord[1] += 1
        prev = 'r'
    elif map_arr[start_coord[0] + 1][start_coord[1]] in ['J', 'L', '|']:
        step += 1
        start_coord[0] += 1
        prev = 'd'
    while map_arr[start_coord[0]][start_coord[1]] != 'S':
        step += 1
        curr = map_arr[start_coord[0]][start_coord[1]]
        if prev == 'u':
            if curr == '|':
                prev = 'u'
                start_coord[0] -= 1
            elif curr == '7':
                prev = 'l'
                start_coord[1] -= 1
            elif curr == 'F':
                prev = 'r'
                start_coord[1] += 1
            continue
        elif prev == 'l':
            if curr == 'L':
                prev = 'u'
                start_coord[0] -= 1
            elif curr == '-':
                prev = 'l'
                start_coord[1] -= 1
            elif curr == 'F':
                prev = 'd'
                start_coord[0] += 1
            continue
        elif prev == 'r':
            if curr == 'J':
                prev = 'u'
                start_coord[0] -= 1
            elif curr == '-':
                prev = 'r'
                start_coord[1] += 1
            elif curr == '7':
                prev = 'd'
                start_coord[0] += 1
            continue
        elif prev == 'd':
            if curr == 'J':
                prev = 'l'
                start_coord[1] -= 1
            elif curr == 'L':
                prev = 'r'
                start_coord[1] += 1
            elif curr == '|':
                prev = 'd'
                start_coord[0] += 1
            continue
    print(int(step/2))

if __name__ == "__main__":
    main()
