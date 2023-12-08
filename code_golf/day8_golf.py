from aocd import get_data; import math; lines = get_data(day=8, year=2023).split("\n");
p = lines[0]; md = {line[0:3]: {'L': line[7:10], 'R': line[12:15]} for line in lines[2:]}
node = 'AAA'; count = 0; nodes = [k for k in md.keys() if k[2] == 'A']; cs = [0]*len(nodes)
for i, n in enumerate(nodes):
    while n[2] != 'Z': n = md[n][p[cs[i]%len(p)]]; cs[i] += 1
print(f'Part 1: {cs[0]}, Part 2: {math.lcm(*cs)}')