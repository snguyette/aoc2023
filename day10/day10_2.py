from aocd import get_data; import numpy as np

def main():
    my_data = get_data(day=10, year=2023)
    map_arr = np.array([list(line) for line in my_data.split("\n")])
    e_arr = np.full((map_arr.shape[0]*2-1, map_arr.shape[1]*2-1), '.')
    start_coord = list(list(zip(*np.where(map_arr == 'S')))[0])

    if map_arr[start_coord[0] - 1][start_coord[1]] in ['7', 'F', '|']:
        start_coord[0] -= 1
        e_arr[start_coord[0]*2 + 1][start_coord[1]*2] = 's'
        prev = 'u'
    elif map_arr[start_coord[0]][start_coord[1] - 1] in ['L', 'F', '-']:
        start_coord[1] -= 1
        e_arr[start_coord[0]*2][start_coord[1]*2 + 1] = 's'
        prev = 'l'
    elif map_arr[start_coord[0]][start_coord[1] + 1] in ['7', 'J', '-']:
        start_coord[1] += 1
        e_arr[start_coord[0]*2][start_coord[1]*2 - 1] = 's'
        prev = 'r'
    elif map_arr[start_coord[0] + 1][start_coord[1]] in ['J', 'L', '|']:
        start_coord[0] += 1
        e_arr[start_coord[0]*2 - 1][start_coord[1]*2] = 's'
        prev = 'd'
    first_dir = prev
    while map_arr[start_coord[0]][start_coord[1]] != 'S':
        curr = map_arr[start_coord[0]][start_coord[1]]
        if curr in ['J', 'L', '7', 'F']:
            e_arr[start_coord[0]*2][start_coord[1]*2] = 'b'
        else:
            e_arr[start_coord[0]*2][start_coord[1]*2] = 's'
        if prev == 'u':
            if curr == '|':
                prev = 'u'
                start_coord[0] -= 1
                e_arr[start_coord[0]*2 + 1][start_coord[1]*2] = 's'
            elif curr == '7':
                prev = 'l'
                start_coord[1] -= 1
                e_arr[start_coord[0]*2][start_coord[1]*2 + 1] = 's'
            elif curr == 'F':
                prev = 'r'
                start_coord[1] += 1
                e_arr[start_coord[0]*2][start_coord[1]*2 - 1] = 's'
            continue
        elif prev == 'l':
            if curr == 'L':
                prev = 'u'
                start_coord[0] -= 1
                e_arr[start_coord[0]*2 + 1][start_coord[1]*2] = 's'
            elif curr == '-':
                prev = 'l'
                start_coord[1] -= 1
                e_arr[start_coord[0]*2][start_coord[1]*2 + 1] = 's'
            elif curr == 'F':
                prev = 'd'
                start_coord[0] += 1
                e_arr[start_coord[0]*2 - 1][start_coord[1]*2] = 's'
            continue
        elif prev == 'r':
            if curr == 'J':
                prev = 'u'
                start_coord[0] -= 1
                e_arr[start_coord[0]*2 + 1][start_coord[1]*2] = 's'
            elif curr == '-':
                prev = 'r'
                start_coord[1] += 1
                e_arr[start_coord[0]*2][start_coord[1]*2 - 1] = 's'
            elif curr == '7':
                prev = 'd'
                start_coord[0] += 1
                e_arr[start_coord[0]*2 - 1][start_coord[1]*2] = 's'
            continue
        elif prev == 'd':
            if curr == 'J':
                prev = 'l'
                start_coord[1] -= 1
                e_arr[start_coord[0]*2][start_coord[1]*2 + 1] = 's'
            elif curr == 'L':
                prev = 'r'
                start_coord[1] += 1
                e_arr[start_coord[0]*2][start_coord[1]*2 - 1] = 's'
            elif curr == '|':
                prev = 'd'
                start_coord[0] += 1
                e_arr[start_coord[0]*2 - 1][start_coord[1]*2] = 's'
            continue
    last_dir = prev
    if (first_dir == last_dir):
        e_arr[start_coord[0]*2][start_coord[1]*2] = 's'
    else:
        e_arr[start_coord[0]*2][start_coord[1]*2] = 'b'
    print(e_arr.shape)
    first = True
    while np.count_nonzero(e_arr=='.') > 0:
        for i, l in enumerate(e_arr):
            for j, v in enumerate(l):
                if v != '.':
                    continue
                if i == 0 or i == e_arr.shape[0] - 1 or j == 0 or j == e_arr.shape[1] - 1:
                    e_arr[i][j] = 'O'
                    continue
                for scan in [np.flip(e_arr[0:i, j]), np.flip(e_arr[i, 0:j]), e_arr[i+1:, j], e_arr[i, j+1:]]:
                    if e_arr[i][j] != '.':
                        break
                    s_count = 0
                    for space in scan:
                        if space == 'O':
                            if s_count % 2 == 0:
                                e_arr[i][j] = 'O'
                                break
                            e_arr[i][j] = 'I'
                            break
                        if space == 'I':
                            if s_count % 2 == 1:
                                e_arr[i][j] = 'O'
                                break
                            e_arr[i][j] = 'I'
                            break
                        if space == 'b':
                            s_count = -1
                            break
                        s_count += 1
    for l in e_arr:
        print(''.join(l))
    count = 0
    for i, l in enumerate(e_arr):
        for j, v in enumerate(l):
            if i % 2 == 0 and j % 2 == 0 and e_arr[i, j] == 'I':
                count += 1
    print(count)

if __name__ == "__main__":
    main()
