from aocd import get_data

def main():
    lines = get_data(day=4, year=2023).split("\n")
    winnings = 0
    for line in lines:
        card_lists = line.split(": ")[1].split(" | ")
        winning_nums = [num for num in card_lists[0].split(" ") if num != '']
        my_nums = [num for num in card_lists[1].split(" ") if num != '']
        wins = sum([1 if num in winning_nums else 0 for num in my_nums])
        winnings += 0 if wins == 0 else 2 ** (wins - 1)
    print(winnings)

if __name__ == "__main__":
    main()
