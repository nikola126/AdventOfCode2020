# Day 8

def booter(cmd_list_func, inc_list_func, visited_func):
    acc_func = 0
    idx = 0
    success_func = True
    # print(f"Max i = {len(cmd_list)-1}")
    while True:
        # print(f"i = {idx}, command: {cmd_list_func[idx]} {inc_list_func[idx]} visited: {visited_func[idx]}")
        if visited_func[idx]:
            success_func = False
            break
        if cmd_list_func[idx] == 'nop':
            visited_func[idx] = True
            idx += 1
        elif cmd_list_func[idx] == 'acc':
            # print(f"Increment acc by {inc_list[i]}")
            visited_func[idx] = True
            acc_func += inc_list_func[idx]
            idx += 1
        elif cmd_list_func[idx] == 'jmp':
            # print(f"Jump to index: {i + inc_list[i]}")
            # no jump? move next by 1
            if inc_list_func[idx] == 0:
                idx += 1
            else:
                idx += inc_list_func[idx]
        else:
            print("Unrecognized Command:", cmd_list_func[idx])
            break
        if idx == len(cmd_list_func):
            break
    return acc_func, success_func


if __name__ == '__main__':

    cmd_list = []  # holds commands
    inc_list = []  # holds increments
    visited = []  # holds status
    for line in open('puzzle_input.txt', 'r').readlines():
        line = line.split(' ')
        cmd_list.append(line[0])
        inc_list.append(int(line[1]))
        visited.append(False)

    print(f"Part One\n")
    # send copies
    cmd_copy = cmd_list[:]
    inc_copy = inc_list[:]
    visited_copy = visited[:]
    acc, success = booter(cmd_copy, inc_copy, visited_copy)

    print("Success:", success)
    print(f"Accumulator: {acc}")

    print(f"\nPart Two\n")

    success = False

    while not success:
        # CHANGE jmp -> nop
        for i in range(0, len(cmd_list)):
            if cmd_list[i] == 'jmp':
                print(f"Attempt to change {cmd_list[i]} at index {i} to nop", '-----' * 5)
                cmd_fix = cmd_list[:]
                cmd_fix[i] = 'nop'
                # print('ORIGINAL:\t', cmd_list)
                # print('FIX:\t\t', cmd_fix)
                inc_fix = inc_list[:]
                vis_fix = visited[:]
                acc, success = booter(cmd_fix, inc_fix, vis_fix)
                # print(success)
            if success:
                print("Last run was successful")
                print("Accumulator: ", acc)
                break
        # print("Can't fix with jmp -> nop")
        # CHANGE nop -> jmp
        for i in range(0, len(cmd_list)):
            if cmd_list[i] == 'nop':
                print(f"Attempt to change {cmd_list[i]} at index {i} to jmp", '-----' * 5)
                cmd_fix = cmd_list[:]
                cmd_fix[i] = 'jmp'
                # print('ORIGINAL:\t', cmd_list)
                # print('FIX:\t\t', cmd_fix)
                inc_fix = inc_list[:]
                vis_fix = visited[:]
                acc, success = booter(cmd_fix, inc_fix, vis_fix)
                # print(success)
            if success:
                print("Last run was successful")
                print("Accumulator: ", acc)
        # print("Can't fix with nop -> jmp")
        break
