from aocd import get_data; import numpy as np; import re; t = 0; g = {}; ls = \
    get_data(day=3, year=2023).split("\n"); c = np.array([list(l) for l in ls], dtype=str)
for i, row in enumerate(c):
    for num in [m for m in re.finditer(r'\d+', ls[i])]:
        vals = c[max(i - 1, 0):min(i + 1, len(ls) - 1) + 1,
            max(num.start(0) - 1, 0):min(num.end(0) + 1, len(ls[i]))].flatten()
        if True in [(not c.isnumeric() and c != '.') for c in vals]: t += int(num[0])
        for j in range(max(i - 1, 0), min(i + 1, len(ls) - 1) + 1):
            for k in range(max(num.start(0) - 1, 0), min(num.end(0) + 1, len(ls[i]))):
                if (j, k) in g and c[j, k] == '*': g[(j, k)].append(int(num[0]))
                elif c[j, k] == '*': g[(j, k)] = [int(num[0])]
sum_of_gears = sum([v[0] * v[1] if len(v) == 2 else 0 for k, v in g.items()])
print(f'Part 1: {t}, Part 2: {sum_of_gears}')