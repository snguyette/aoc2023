from aocd import get_data
import itertools

def main():
    my_data = get_data(day=12, year=2023)
    lines = my_data.split("\n")
    # print(len(lines))
    total = 0
    lines_to_disp = 10
    for line in lines:
        # print(line)
        line_split = line.split(' ')
        spring_data = line_split[0]
        group_data = line_split[1].split(',')
        u_count = sum([1 for c in spring_data if c == '?'])
        # print(u_count)
        u_possibilities = itertools.product('.#', repeat=u_count)
        successful_combos = []
        for p in u_possibilities:
            # print(p)
            curr = 0
            group_num = 0
            success = True
            u_idx = 0
            for s in spring_data:
                if s == '#':
                    if group_num >= len(group_data):
                        success = False
                        break
                    curr += 1
                elif s == '?':
                    if p[u_idx] == '#':
                        if group_num >= len(group_data):
                            success = False
                            break
                        curr += 1
                    else:
                        if curr > 0:
                            # print(group_data[group_num])
                            # print(curr)
                            if curr != int(group_data[group_num]):
                                success = False
                                # print("mismatch")
                                break
                            curr = 0
                            group_num += 1
                    u_idx += 1
                else:
                    if curr > 0:
                        # print(group_data[group_num])
                        # print(curr)
                        if curr != int(group_data[group_num]):
                            success = False
                            # print("mismatch")
                            break
                        curr = 0
                        group_num += 1
            if group_num < len(group_data):
                if group_num == len(group_data) - 1:
                    if curr != int(group_data[group_num]):
                        success = False
                else:
                    success = False
            if success:
                # print(f"{p}: success")
                total += 1
                successful_combos.append(p)
        print(len(successful_combos))
            # else:
            #     print("fail")
        # break
        # print(group_data)
        # print(spring_data)
        # for c in successful_combos:
        #     new_str = ""
        #     idx = 0
        #     for s in spring_data:
        #         if s == '?':
        #             new_str += c[idx]
        #             idx += 1
        #         else:
        #             new_str += s
        #     print(new_str)
        # if lines_to_disp == 0:
        #     break
        # else:
        #     lines_to_disp -= 1

    print(total)


if __name__ == "__main__":
    main()
