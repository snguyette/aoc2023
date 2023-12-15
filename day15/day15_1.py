from aocd import get_data

def main():
    my_data = get_data(day=15, year=2023)
    # print(my_data)
    sequence = my_data.split(',')
    total = 0
    mod_val = 256
    for s in sequence:
        curr = 0
        for c in s:
            curr += ord(c)
            curr *= 17
            curr = curr % mod_val
        total += curr
    # lines = my_data.split("\n")
    print(total)

if __name__ == "__main__":
    main()
