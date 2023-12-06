from aocd import get_data

def main():
    my_data = get_data(day=5, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    lines.append('')
    # print(lines)
    # exit()
    seeds = [int(seed) for seed in lines[0].split(': ')[1].split(' ')]
    print(seeds)
    map_list = []
    for line in lines[2:]:
        if line == '':
            # print(map_list)
            for i, seed in enumerate(seeds):
                for map_dict in map_list:
                    if map_dict['src_start'] <= seed <= map_dict['src_end']:
                        print(f'Found range for {seed}: {map_dict}')
                        seeds[i] = map_dict['dst_start'] + (seed - map_dict['src_start'])
                        break
            map_list = []
            print(seeds)
            # break
        elif line[0].isalpha():
            continue
        else:
            line_parse = line.split(' ')
            map_list.append(
                {
                    'src_start': int(line_parse[1]),
                    'src_end': int(line_parse[1]) + int(line_parse[2]) - 1,
                    'dst_start': int(line_parse[0])
                })
    print(min(seeds))

if __name__ == "__main__":
    main()
