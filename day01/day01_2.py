from aocd import get_data
import re

NUM_WORDS = {
    "zero": 0, 
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def main():
    my_data = get_data(day=1, year=2023)
    lines = my_data.split("\n")
    print(len(lines))
    total = 0
    for line in lines:
        nums = [m for m in re.findall(r'(?=(1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine|zero))', line)]
        for i, num in enumerate(nums):
            if num.isnumeric():
                nums[i] = int(num)
            else:
                nums[i] = NUM_WORDS[num]
        if nums:
            total += int(f'{nums[0]}{nums[-1]}')
    print(total)


if __name__ == "__main__":
    main()