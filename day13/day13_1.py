from aocd import get_data
import numpy as np

def main():
    my_data = get_data(day=13, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    # print(len(lines))
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
    for m in mirrors:
        print(m)
        h_sym = False
        # check horizontal symmetry
        for i in range(len(m) - 1):
            sym = True
            s = i
            e = i + 1
            while s >= 0 and e < len(m) and sym:
                sym = False not in [x == y for x, y in zip(m[s], m[e])]
                s -= 1
                e += 1
            if sym:
                h_sym_count += i + 1
                h_sym = True
                print(f'Horizontal symmetry at i={i+1}')
                break
        if h_sym:
            continue
        mt = m.T
        # check vertical symmetry
        for i in range(len(mt) - 1):
            sym = True
            s = i
            e = i + 1
            while s >= 0 and e < len(mt) and sym:
                sym = False not in [x == y for x, y in zip(mt[s], mt[e])]
                s -= 1
                e += 1
            if sym:
                v_sym_count += i + 1
                print(f'Vertical symmetry at i={i+1}')
                break
    print(h_sym_count*100 + v_sym_count)

if __name__ == "__main__":
    main()
