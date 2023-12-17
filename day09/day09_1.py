from aocd import get_data

def main():
    my_data = get_data(day=9, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    # print(len(lines))
    total = 0
    for line in lines:
        # print(line)
        vals = [int(num) for num in line.split(' ')]
        for i in range(0, len(vals) - 1):
            for j in range(i+1):
                vals[i - j] = vals[(i -j)+1] - vals[i - j]
        total += sum(vals)
    print(total)

if __name__ == "__main__":
    main()
