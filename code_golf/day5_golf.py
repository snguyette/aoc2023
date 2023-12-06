from aocd import get_data
lines = get_data(day=5, year=2023).split("\n") + ['']
seeds = [int(seed) for seed in lines[0].split(': ')[1].split(' ')]
ranges = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
map_list = []
for line in lines[2:]:
    if line == '':
        for i, seed in enumerate(seeds):
            for map_dict in map_list:
                if map_dict['src_start'] <= seed <= map_dict['src_end']:
                    seeds[i] = map_dict['dst_start'] + (seed - map_dict['src_start'])
                    break
            for i, r in enumerate(ranges):
                for m in map_list:
                    if r[0] <= m['src_end'] and r[1] >= m['src_start']:
                        if r[0] < m['src_start']: ranges.append((r[0], m['src_start'] - 1))
                        if r[1] > m['src_end']: ranges.append((m['src_end'] + 1, r[1]))
                        ranges[i] = (
                            m['dst_start'] + max(r[0], m['src_start']) - m['src_start'],
                            m['dst_start'] + min(r[1], m['src_end']) - m['src_start'])
                    break
        map_list = []
    elif line[0].isalpha(): continue
    else:
        line_parse = line.split(' ')
        map_list.append({'src_start': int(line_parse[1]), 'src_end': int(line_parse[1]) + \
                         int(line_parse[2]) - 1, 'dst_start': int(line_parse[0])})
print(f'Part 1: {min(seeds)}, Part 2: {min([r[0] for r in ranges])}')