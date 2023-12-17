from aocd import get_data
import math

def main():
    my_data = get_data(day=8, year=2023)
    lines = my_data.split("\n")
    pathway = lines[0]
    print(pathway)
    map_dict = {}
    start_nodes = []
    for line in lines[2:]:
        start = line[0:3]
        if start[2] == 'A':
            start_nodes.append(start)
        left = line[7:10]
        right = line[12:15]
        map_dict[start] = {'L': left, 'R': right}
    counts = []
    for node in start_nodes:
        count = 0
        while node[2] != 'Z':
            node = map_dict[node][pathway[count % len(pathway)]]
            count += 1
        counts.append(count)
    print(math.lcm(*counts))

if __name__ == "__main__":
    main()
