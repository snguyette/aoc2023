from aocd import get_data; import numpy as np; from numpy import count_nonzero as cn
m = np.array([list(l) for l in get_data(day=10, year=2023).split("\n")]); n=m.shape[1]*2-1
e = np.full((n, n), '.'); sc = list(list(zip(*np.where(m == 'S')))[0]); oi = ['O', 'I']
if m[sc[0] - 1][sc[1]] in ['7', 'F', '|']:
    sc[0] -= 1; e[sc[0]*2 + 1][sc[1]*2] = 's'; p = 'u'; f = p
elif m[sc[0]][sc[1] - 1] in ['L', 'F', '-']:
    sc[1] -= 1; e[sc[0]*2][sc[1]*2 + 1] = 's'; p = 'l'; f = p
elif m[sc[0]][sc[1] + 1] in ['7', 'J', '-']:
    sc[1] += 1; e[sc[0]*2][sc[1]*2 - 1] = 's'; p = 'r'; f = p
while m[sc[0]][sc[1]] != 'S':
    c = m[sc[0]][sc[1]]; e[sc[0]*2][sc[1]*2] = 'b' if c in ['J', 'L', '7', 'F'] else 's'
    if p == 'u' and c == '|': p = 'u'; sc[0] -= 1; e[sc[0]*2 + 1][sc[1]*2] = 's'; continue
    if p == 'u' and c == '7': p = 'l'; sc[1] -= 1; e[sc[0]*2][sc[1]*2 + 1] = 's'; continue
    if p == 'u' and c == 'F': p = 'r'; sc[1] += 1; e[sc[0]*2][sc[1]*2 - 1] = 's'; continue
    if p == 'l' and c == 'L': p = 'u'; sc[0] -= 1; e[sc[0]*2 + 1][sc[1]*2] = 's'; continue
    if p == 'l' and c == '-': p = 'l'; sc[1] -= 1; e[sc[0]*2][sc[1]*2 + 1] = 's'; continue
    if p == 'l' and c == 'F': p = 'd'; sc[0] += 1; e[sc[0]*2 - 1][sc[1]*2] = 's'; continue
    if p == 'r' and c == 'J': p = 'u'; sc[0] -= 1; e[sc[0]*2 + 1][sc[1]*2] = 's'; continue
    if p == 'r' and c == '-': p = 'r'; sc[1] += 1; e[sc[0]*2][sc[1]*2 - 1] = 's'; continue
    if p == 'r' and c == '7': p = 'd'; sc[0] += 1; e[sc[0]*2 - 1][sc[1]*2] = 's'; continue
    if c == 'J': p = 'l'; sc[1] -= 1; e[sc[0]*2][sc[1]*2 + 1] = 's'; continue
    if c == 'L': p = 'r'; sc[1] += 1; e[sc[0]*2][sc[1]*2 - 1] = 's'; continue
    if c == '|': p = 'd'; sc[0] += 1; e[sc[0]*2 - 1][sc[1]*2] = 's'; continue
print(f'Part 1: {int((cn(e != ".")+1)/4)}'); e[sc[0]*2][sc[1]*2] = 's' if (f==p) else 'b'
for i, l in enumerate(e):
    for j, v in enumerate(l):
        if v != '.': continue
        if i*j == 0 or i == e.shape[0] - 1 or j == e.shape[1] - 1:
            e[i][j] = 'O'; continue
        for s in [np.flip(e[0:i, j]), np.flip(e[i, 0:j]), e[i+1:, j], e[i, j+1:]]:
            if e[i][j] != '.': break
            s_count = 0
            for space in s:
                if space in oi: e[i][j] = oi[(s_count % 2) != oi.index(space)]; break
                if space == 'b': break
                s_count += 1
print(f'Part 2: {cn(e[::2, ::2]=="I", keepdims=False)}')