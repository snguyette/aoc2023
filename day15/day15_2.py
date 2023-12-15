from aocd import get_data

def main():
    my_data = get_data(day=15, year=2023)
    # print(my_data)
    sequence = my_data.split(',')
    total = 0
    mod_val = 256
    boxes = [[] for i in range(256)]
    # print(boxes)
    # exit()
    lines_to_disp = 10
    for s in sequence:
        # print(s)
        if '-' in s:
            label = s[:-1]
            op = '-'
        else:
            label = s.split('=')[0]
            op = '='
            focal_length = int(s.split('=')[1])
        # print(label)
        # print(op)
        box_num = 0
        for c in label:
            box_num += ord(c)
            box_num *= 17
            box_num = box_num % mod_val
        # print(box_num)
        if op == '-':
            for i, lens in enumerate(boxes[box_num]):
                if lens['label'] == label:
                    boxes[box_num].pop(i)
                    break
        else:
            found_match = False
            for i, lens in enumerate(boxes[box_num]):
                if lens['label'] == label:
                    lens['focal_length'] = focal_length
                    found_match = True
                    break
            if not found_match:
                boxes[box_num].append({
                    'label': label,
                    'focal_length': focal_length
                })
        # print(boxes)
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            total += (i+1) * (j+1) * lens['focal_length']
    print(total)

if __name__ == "__main__":
    main()
