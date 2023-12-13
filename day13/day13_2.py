from aocd import get_data
import numpy as np

def opp(c):
    if c == '.':
        return '#'
    return '.'

def find_sym(pattern, ignore=None):
    if ignore:
        ignore_i = ignore['idx']
        ignore_type = ignore['sym_type']
        deep = True
    else:
        ignore_i = -1
        ignore_type = 'U'
        deep = False
    h_sym = False
    sym_type = 'U'
    idx = -1
    # check horizontal symmetry
    for i in range(len(pattern) - 1):
        if ignore_type == 'H' and ignore_i == i:
            continue
        sym = True
        s = i
        e = i + 1
        while s >= 0 and e < len(pattern) and sym:
            sym = False not in [x == y for x, y in zip(pattern[s], pattern[e])]
            s -= 1
            e += 1
        if sym:
            sym_type = 'H'
            idx = i
            h_sym = True
            break
    if not h_sym:
        pattern_t = pattern.T
        # check vertical symmetry
        for i in range(len(pattern_t) - 1):
            if ignore_type == 'V' and ignore_i == i:
                continue
            sym = True
            s = i
            e = i + 1
            while s >= 0 and e < len(pattern_t) and sym:
                sym = False not in [x == y for x, y in zip(pattern_t[s], pattern_t[e])]
                s -= 1
                e += 1
            if sym:
                sym_type = 'V'
                idx = i
                break
    if deep:
        return (sym_type, idx + 1)
    else:
        ignore_dict = {'sym_type': sym_type, 'idx': idx}
        for i in range(len(pattern)):
            for j in range(len(pattern.T)):
                new_pattern = np.copy(pattern)
                new_pattern[i, j] = opp(new_pattern[i, j])
                st, idx = find_sym(new_pattern, ignore_dict)
                if st != 'U':
                    return (st, idx)


def main():
    my_data = get_data(day=13, year=2023)
    lines = my_data.split("\n")
    mirrors = []
    curr = []
    for line in lines:
        if line:
            curr.append(list(line))
        else:
            mirrors.append(np.array(curr))
            curr = []
    mirrors.append(np.array(curr))
    print(mirrors[0])
    print(len(mirrors))
    h_sym_count = 0
    v_sym_count = 0
    for i, m in enumerate(mirrors):
        sym_type, idx = find_sym(m)
        if sym_type == 'H':
            h_sym_count += idx
        elif sym_type == 'V':
            v_sym_count += idx
        else:
            print(f"No new symmetry found for mirror {i}: \n{m}")
    print(h_sym_count*100 + v_sym_count)

if __name__ == "__main__":
    main()
