from aocd import get_data; import re; import numpy as np
ts = [m for m in re.findall(r'\d+', get_data(day=6, year=2023).split("\n")[0])]
rs = [m for m in re.findall(r'\d+', get_data(day=6, year=2023).split("\n")[1])]
w = [sum([1 for i in range(int(t) + 1) if (int(t) - i)*i > int(r)]) for t, r in zip(ts, rs)]
times = int(''.join(ts)); recs = int(''.join(rs)); print(f'Part 1: {w}')
print(f'Part 2: {sum(1 for i in range(int(times) + 1) if (int(times) - i)*i > int(recs))}')