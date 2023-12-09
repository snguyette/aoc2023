from aocd import get_data; import re; total1, t2 = 0, 0; nw = {"zero": 0, "one": 1,
"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
nr = r'(?=(1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine|zero))'
lines = get_data(day=1, year=2023).split("\n")
t1 = sum([int(f'{n[0]}{n[-1]}') for l in lines for n in [[c for c in l if c.isnumeric()]]])
t2 = sum([int(f'{n[0]}{n[-1]}') for l in lines for n in [[int(m) if m.isnumeric() else nw[m]
    for m in re.findall(nr, l)]]]); print(f'Part 1: {t1}, Part 2: {t2}')