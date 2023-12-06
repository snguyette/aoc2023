from aocd import get_data; MAX_VALS = {'red': 12, 'green': 13, 'blue': 14}; games = [0, 0]
for line in get_data(day=2, year=2023).split("\n"):
    c_dict = {'blue': [], 'red': [], 'green': []}
    for r in line.split(': ')[1].split('; '):
        for c in r.split(', '): c_dict[c.split(' ')[1]].append(int(c.split(' ')[0]))
    if False not in [max(c_dict[col]) <= MAX_VALS[col] for col in ['red', 'green', 'blue']]:
        games[0] += int(line.split(': ')[0].split(' ')[1])
    games[1] += max(c_dict['blue']) * max(c_dict['red']) * max(c_dict['green'])
print(f'Part 1: {games[0]}, Part 2: {games[1]}')