from aocd import get_data; from collections import Counter; from functools import cmp_to_key
rs = [['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'],
      ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']]; first_run = 1
def compare_hands(hand1, hand2):
    h1 = Counter(hand1[0]).most_common(); h2 = Counter(hand2[0]).most_common()
    if not first_run:
        j1 = dict(h1)['J'] if 'J' in dict(h1) else 0; h1 = [c for c in h1 if c[0] != 'J']
        j2 = dict(h2)['J'] if 'J' in dict(h2) else 0; h2 = [c for c in h2 if c[0] != 'J']
    else: j1, j2 = 0, 0
    if j1 == 5: return -1 if h2[0][1] + j2 == 5 else 1
    if j2 == 5: return 1 if h1[0][1] + j1 == 5 else -1
    if h1[0][1] + j1 != h2[0][1] + j2: return (h1[0][1] + j1) - (h2[0][1] + j2)
    elif len(h1) > 1 and h1[1][1] != h2[1][1]: return h1[1][1] - h2[1][1]
    for v1, v2 in zip(hand1[0], hand2[0]):
        if diff:= rs[first_run].index(v1) - rs[first_run].index(v2): return diff
hs = [(h.split(' ')[0], h.split(' ')[1]) for h in get_data(day=7, year=2023).split("\n")]
s_hs = sorted(hs, key=cmp_to_key(compare_hands)); first_run = 0
total = sum([(i+1)*int(h[1]) for i, h in enumerate(s_hs)]); print(f"Part 1: {total}")
s_hs = sorted(hs, key=cmp_to_key(compare_hands))
total = sum([(i+1)*int(h[1]) for i, h in enumerate(s_hs)]); print(f"Part 2: {total}")