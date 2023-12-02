from aocd import get_data

def main():
    my_data = get_data(day=1, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    print(len(lines))

if __name__ == "__main__":
    main()
