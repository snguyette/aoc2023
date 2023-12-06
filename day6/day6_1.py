from aocd import get_data
import re
import numpy as np

def main():
    my_data = get_data(day=6, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    times = [int(m) for m in re.findall(r'\d+', lines[0])]
    records = [int(m) for m in re.findall(r'\d+', lines[1])]
    assert len(times) == len(records)
    race_wins = []
    for t, r in zip(times, records):
        wins = 0
        for i in range(t + 1):
            if (t - i)*i > r:
                wins += 1
        race_wins.append(wins)
    print(np.prod(race_wins))

if __name__ == "__main__":
    main()
