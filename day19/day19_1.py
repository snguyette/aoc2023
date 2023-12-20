from aocd import get_data

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
            # print(rule_dict)
            # exit()
        else:
            vals = line.split('{')[1][:-1]
            item = {}
            for v in vals.split(','):
                # print(v)
                v_split = v.split('=')
                # print(v_split)
                item[v_split[0]] = int(v_split[1])
            curr = 'in'
            det = False
            verdict = None
            while not det:
                ruleset = rule_dict[curr]
                for r in ruleset:
                    if r['rule_type'] == 'comparison':
                        if r['op'] == '>':
                            if item[r['tgt']] > r['val']:
                                curr = r['jmp']
                                if curr in ['R', 'A']:
                                    det = True
                                    verdict = curr
                                break
                        else:
                            if item[r['tgt']] < r['val']:
                                curr = r['jmp']
                                if curr in ['R', 'A']:
                                    det = True
                                    verdict = curr
                                break
                    elif r['rule_type'] == 'jump':
                        curr = r['jmp']
                        break
                    else:
                        det = True
                        verdict = r['det']
                        break
            if det:
                if verdict == 'A':
                    total += item['x'] + item['m'] + item['a'] + item['s']
    print(total)

                            

                    

if __name__ == "__main__":
    main()
