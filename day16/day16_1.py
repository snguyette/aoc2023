from aocd import get_data
import numpy as np

BACKSLASH_CONV = {
    'u': 'l',
    'd': 'r',
    'l': 'u',
    'r': 'd'
}

FORWARDSLASH_CONV = {
    'u': 'r',
    'd': 'l',
    'l': 'd',
    'r': 'u'
}

FOUND_MIRRORS = {}

def next_pos(pos, direction):
    if direction == 'l':
        return (pos[0], pos[1]-1) 
    if direction == 'r':
        return (pos[0], pos[1]+1) 
    if direction == 'u':
        return (pos[0]-1, pos[1]) 
    return (pos[0]+1, pos[1]) 

def follow_beam(pos, direction, grid, energy):
    hit_wall = False
    while not hit_wall:
        print(pos)
        if pos[0] >= grid.shape[0] or pos[0] < 0 or pos[1] >= grid.shape[1] or pos[1] < 0:
            hit_wall = True
            return
        energy[pos[0], pos[1]] += 1
        curr_symbol = grid[pos[0], pos[1]]
        if curr_symbol == '|':
            if direction in ['l', 'r']:
                if pos in FOUND_MIRRORS:
                    if direction in FOUND_MIRRORS[pos]:
                        return
                    else:
                        FOUND_MIRRORS[pos].append(direction)
                else:
                    FOUND_MIRRORS[pos] = [direction]
                follow_beam((pos[0], pos[1]), 'd', grid, energy)
                direction = 'u'
        elif curr_symbol == '-':
            if direction in ['u', 'd']:
                if pos in FOUND_MIRRORS:
                    if direction in FOUND_MIRRORS[pos]:
                        return
                    else:
                        FOUND_MIRRORS[pos].append(direction)
                else:
                    FOUND_MIRRORS[pos] = [direction]
                follow_beam((pos[0], pos[1]), 'l', grid, energy)
                direction = 'r'
        elif curr_symbol == '\\':
            if pos in FOUND_MIRRORS:
                if direction in FOUND_MIRRORS[pos]:
                    return
                else:
                    FOUND_MIRRORS[pos].append(direction)
            else:
                FOUND_MIRRORS[pos] = [direction]
            direction = BACKSLASH_CONV[direction]
        elif curr_symbol == '/':
            if pos in FOUND_MIRRORS:
                if direction in FOUND_MIRRORS[pos]:
                    return
                else:
                    FOUND_MIRRORS[pos].append(direction)
            else:
                FOUND_MIRRORS[pos] = [direction]
            direction = FORWARDSLASH_CONV[direction]
        pos = next_pos(pos, direction)


def main():
    my_data = get_data(day=16, year=2023)
    # my_data = ".|...\\....\n|.-.\\.....\n.....|-...\n........|.\n..........\n.........\\\n..../.\\\\..\n.-.-/..|..\n.|....-|.\\\n..//.|...."
    print(my_data)
    # exit()
    lines = my_data.split("\n")
    # for line in lines:
        # print(len(line))
    # print(lines)
    # exit()
    # print(len(lines))
    grid = np.array([list(line) for line in lines])
    # print(grid.shape)
    # exit()
    # for line in lines:
    #     grid.append(np.array(list(line)))
    # grid = np.array(grid)
    # print(grid.shape)
    start_pos = (0, 0)
    start_dir = 'r'
    energy = np.zeros(grid.shape)
    follow_beam(start_pos, start_dir, grid, energy)
    total = np.count_nonzero(energy > 0)
    print(total)

if __name__ == "__main__":
    main()
