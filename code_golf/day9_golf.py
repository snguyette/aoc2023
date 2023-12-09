from aocd import get_data; total1 = 0; total2 = 0;
for line in get_data(day=9, year=2023).split("\n"):
    vals = [int(num) for num in line.split(' ')]; fv = [vals[0]]; val = 0
    for i in range(0, len(vals) - 1):
        for j in range(i+1): vals[i-j] = vals[(i-j)+1] - vals[i-j]
        fv.append(vals[0])      
    for i in range(len(fv), 0, -1): val = fv[i - 1] - val
    total1 += sum(vals); total2 += val
print(f"Part 1: {total1}, Part 2: {total2}")