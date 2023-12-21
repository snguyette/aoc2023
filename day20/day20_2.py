from aocd import get_data
from queue import Queue

LO = 0
HI = 1

def main():
    my_data = get_data(day=20, year=2023)
    # lines = ["broadcaster -> a, b, c", r"%a -> b", r"%b -> c", r"%c -> inv", "&inv -> a"]
    # print(my_data)
    lines = my_data.split("\n")
    # print(len(lines))
    # exit()
    # print(len(lines))
    modules = {}
    conj_list = []
    for line in lines:
        line_data = line.split(' -> ')
        module_name = line_data[0]
        module_conns = line_data[1].split(', ')
        if module_name[0] == '%':
            module_name = module_name[1:]
            modules[module_name] = {'conns': module_conns}
            modules[module_name]['type'] = 'ff'
            modules[module_name]['state'] = 'off'
            modules[module_name]['num'] = 0
            modules[module_name]['count_list'] = []
        elif module_name[0] == '&':
            module_name = module_name[1:]
            modules[module_name] = {'conns': module_conns}
            conj_list.append(module_name)
            modules[module_name]['type'] = 'conj'
            modules[module_name]['prev_signals'] = {}
            modules[module_name]['num'] = 0
            modules[module_name]['count_list'] = []
        else:
            modules[module_name] = {'conns': module_conns}
            modules[module_name]['type'] = 'bc'
            modules[module_name]['num'] = 0
            modules[module_name]['count_list'] = []
    for k, v in modules.items():
        for conn in v['conns']:
            if conn in conj_list:
                modules[conn]['prev_signals'][k] = LO
    for k, v in modules.items():
        print(f'{k}: {v}')
    pulse_q = Queue()
    presses = 1000
    pulse_counts = {
        LO: 0,
        HI: 0
    }
    lo_rx = False
    count = 0
    while not lo_rx:
        for v in modules.values():
            v['num'] = 0
        count += 1
        pulse_q.put((LO, 'broadcaster', 'button'))
        pulse_counts[LO] += 1
        while not pulse_q.empty():
            # print(pulse_q.queue)
            (pulse_type, name, sent_by) = pulse_q.get()
            if name == 'rx':
                if pulse_type == LO:
                    lo_rx = True
                continue
            # print(f'{name}: {pulse_type}')
            module = modules[name]
            if pulse_type == HI:
                module['num'] += 1
            if module['type'] == 'bc':
                for m in module['conns']:
                    pulse_q.put((pulse_type, m, name))
                    pulse_counts[pulse_type] += 1
            elif module['type'] == 'ff':
                if pulse_type == LO:
                    if module['state'] == 'off':
                        module['state'] = 'on'
                        for m in module['conns']:
                            pulse_q.put((HI, m, name))
                            pulse_counts[HI] += 1
                    else:
                        module['state'] = 'off'
                        for m in module['conns']:
                            pulse_q.put((LO, m, name))
                            pulse_counts[LO] += 1
            else:
                module['prev_signals'][sent_by] = pulse_type
                send_hi = True
                # print(module['prev_signals'])
                for k, v in modules[name]['prev_signals'].items():
                    if v == LO:
                        send_hi = False
                        for m in module['conns']:
                            pulse_q.put((HI, m, name))
                            pulse_counts[HI] += 1
                        break
                if send_hi:
                    for m in module['conns']:
                        pulse_q.put((LO, m, name))
                        pulse_counts[LO] += 1
        for k, v in modules.items():
            # print(f"{v['type']}{k}: {v['num']}")
            v['count_list'].append(v['num'])
        if count == 20:
            break
    for k, v in modules.items():
            # print(f"{v['type']}{k}: {v['count_list']}\t\t{v['conns']}")
            print(f"{v['type']}{k}: {v['count_list']} \t\t{len(v['conns'])}")
    # print(count)

if __name__ == "__main__":
    main()
