from aocd import get_data
import numpy as np

def main():
    my_data = get_data(day=14, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    # print(len(lines))
    platform = []
    for line in lines:
        platform.append(np.array(list(line)))
    platform = np.array(platform)
    # print(platform)
    max_load = platform.shape[1]
    total_load = 0
    for col in platform.T:
        anchor = max_load
        rock_count = 0
        for j, space in enumerate(col):
            if space == '#':
                for i in range(rock_count):
                    total_load += anchor - i
                rock_count = 0
                anchor = max_load - (j + 1)
            elif space == 'O':
                rock_count += 1
        for i in range(rock_count):
            total_load += anchor - i
    print(total_load)


if __name__ == "__main__":
    main()
