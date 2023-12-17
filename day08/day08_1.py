from aocd import get_data

def main():
    my_data = get_data(day=8, year=2023)
    print(my_data)
    # exit()
    lines = my_data.split("\n")
    # print(len(lines))
    pathway = lines[0]
    print(pathway)
    map_dict = {}
    for line in lines[2:]:
        start = line[0:3]
        left = line[7:10]
        right = line[12:15]
        map_dict[start] = {'L': left, 'R': right}
    # curr_node = lines[2][0:3]
    curr_node = 'AAA'
    # print(map_dict)
    # print(curr_node)
    
    # curr_idx = 0
    count = 0
    # timeout = 200
    while curr_node != 'ZZZ':
        curr_node = map_dict[curr_node][pathway[count % len(pathway)]]
        count += 1
        if curr_node == 'ZZZ':
            print(curr_node)
    print(count)

if __name__ == "__main__":
    main()
