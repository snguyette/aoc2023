from aocd import get_data

def main():
    my_data = get_data(day=1, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    print(len(lines))
    total = 0
    for line in lines:
        nums = []
        for c in line:
            if c.isnumeric():
                nums.append(c)
        if nums:
            total += int(f'{nums[0]}{nums[-1]}')
    print(total)

if __name__ == "__main__":
    main()