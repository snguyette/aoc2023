from aocd import get_data
import re
import numpy as np

def main():
    my_data = get_data(day=6, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    times = int(''.join([m for m in re.findall(r'\d+', lines[0])]))
    records = int(''.join([m for m in re.findall(r'\d+', lines[1])]))
    wins = 0
    for i in range(times + 1):
        if (times-i) * i > records:
            wins += 1
    print(wins)

if __name__ == "__main__":
    main()
