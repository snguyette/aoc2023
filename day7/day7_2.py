from aocd import get_data
from collections import Counter

rank_list = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def get_hand_type(hand_counts):
    hand_dict = dict(hand_counts)
    j_count = hand_dict['J'] if 'J' in hand_dict else 0
    new_hand_counts = [hand_count for hand_count in hand_counts if hand_count[0] != 'J']
    if new_hand_counts:
        if new_hand_counts[0][1] + j_count == 5:
            return '5k'
        if new_hand_counts[0][1] + j_count == 4:
            return '4k'
        if new_hand_counts[0][1] + j_count == 3:
            if new_hand_counts[1][1] == 2:
                return 'fh'
            else:
                return '3k'
        if new_hand_counts[0][1] + j_count == 2:
            if new_hand_counts[1][1] == 2:
                return '2p'
            else:
                return '1p'
        return 'hc'
    else:
        return '5k'

def compare_hands(hand1, hand2): # first better = True, second better = False
    for h1, h2 in zip(hand1, hand2):
        if rank_list.index(h1) != rank_list.index(h2):
            return rank_list.index(h1) > rank_list.index(h2)
    return True # Should never see this case, hands would be identical

def sort_list(hand_list):
    for i in range(len(hand_list)):
        max_idx = i
        for j in range(i + 1, len(hand_list)):
            if compare_hands(hand_list[j][0], hand_list[max_idx][0]):
                max_idx = j
        hand_list[i], hand_list[max_idx] = hand_list[max_idx], hand_list[i]
    return hand_list

def main():
    my_data = get_data(day=7, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    print(len(lines))
    hand_types = {
        '5k': [],
        '4k': [],
        'fh': [],
        '3k': [],
        '2p': [],
        '1p': [],
        'hc': []
    }
    for line in lines:
        # print(line)
        hand = line.split(' ')[0]
        bid = line.split(' ')[1]
        hand_counts = Counter(list(hand))
        hand_type = get_hand_type(hand_counts.most_common())
        hand_types[hand_type].append((hand, bid))
    all_hands = []
    for k, v in hand_types.items():
        print(k)
        all_hands = all_hands + sort_list(v)
        # hand_types[k] = sort_list(v)
    total = 0
    for i, (_, score) in zip(list(range(1000, 0, -1)), all_hands):
        total += i * int(score)
    print(total)
    # print(hand_types)

if __name__ == "__main__":
    main()
