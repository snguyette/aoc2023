from aocd import get_data
import queue

def main():
    my_data = get_data(day=19, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    # print(len(lines))
    get_rules = True
    rule_dict = {}
    total = 0
    for line in lines:
        print(line)
        if line == '':
            get_rules = False
            continue
        if get_rules:
            rule_name = line.split('{')[0]
            rules = line.split('{')[1][:-1]
            rule_dict[rule_name] = []
            for r in rules.split(','):
                if '>' in r:
                    rule_type = 'comparison'
                    jmp = r.split(':')[1]
                    tgt = r.split(':')[0].split('>')[0]
                    val = int(r.split(':')[0].split('>')[1])
                    op = '>'
                    rule_dict[rule_name].append({'rule_type': rule_type, 'tgt':tgt, 'val':val, 'op':op, 'jmp':jmp})
                elif '<' in r:
                    rule_type = 'comparison'
                    jmp = r.split(':')[1]
                    tgt = r.split(':')[0].split('<')[0]
                    val = int(r.split(':')[0].split('<')[1])
                    op = '<'
                    rule_dict[rule_name].append({'rule_type': rule_type, 'tgt':tgt, 'val':val, 'op':op, 'jmp':jmp})
                else:
                    if r in ['R', 'A']:
                        rule_type = 'terminate'
                        rule_dict[rule_name].append({'rule_type': rule_type, 'det': r})
                    else:
                        rule_type = 'jump'
                        rule_dict[rule_name].append({'rule_type': rule_type, 'jmp': r})
        else:
            break
    rule_q = queue.Queue()
    starting_vals = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }
    starting_ruleset = 'in'
    rule_q.put((starting_ruleset, starting_vals))
    while not rule_q.empty():
        (ruleset, vals) = rule_q.get()
        if ruleset in ['A', 'R']:
            if ruleset == 'A':
                total += (vals['x'][1]-vals['x'][0]+1)*(vals['m'][1]-vals['m'][0]+1)*(vals['a'][1]-vals['a'][0]+1)*(vals['s'][1]-vals['s'][0]+1)
            continue
        rule_list = rule_dict[ruleset]
        for r in rule_list:
            if r['rule_type'] == 'comparison':
                new_vals = vals.copy()
                if r['op'] == '>':
                    tgt = r['tgt']
                    if vals[tgt][1] > r['val']:
                        new_vals[tgt] = (max(vals[tgt][0], r['val']+1), vals[tgt][1])
                        rule_q.put((r['jmp'], new_vals))
                        if vals[tgt][0] <= r['val']:
                            vals[tgt] = (vals[tgt][0], r['val'])
                else:
                    tgt = r['tgt']
                    if vals[tgt][0] < r['val']:
                        new_vals[tgt] = (vals[tgt][0], min(vals[tgt][1], r['val']-1))
                        rule_q.put((r['jmp'], new_vals))
                        if vals[tgt][1] >= r['val']:
                            vals[tgt] = (r['val'], vals[tgt][1])
            elif r['rule_type'] == 'jump':
                rule_q.put((r['jmp'], vals))
            else:
                if r['det'] == 'A':
                    total += (vals['x'][1]-vals['x'][0]+1)*(vals['m'][1]-vals['m'][0]+1)*(vals['a'][1]-vals['a'][0]+1)*(vals['s'][1]-vals['s'][0]+1)
    print(total)

if __name__ == "__main__":
    main()
