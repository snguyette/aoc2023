from aocd import get_data
winnings = 0
lines = get_data(day=4, year=2023).split("\n")
copies = [1]*len(lines)
for i, line in enumerate(lines):
    card_lists = line.split(": ")[1].split(" | ")
    winning_nums = [num for num in card_lists[0].split(" ") if num != '']
    my_nums = [num for num in card_lists[1].split(" ") if num != '']
    wins = sum([1 if num in winning_nums else 0 for num in my_nums])
    winnings += 0 if wins == 0 else 2 ** (wins - 1)
    for j in range(1, wins + 1):
        if i + j < len(lines):
            copies[i + j] += copies[i]
print(f'Part 1: {winnings}, Part 2: {sum(copies)}')