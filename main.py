# Day 13

if __name__ == '__main__':

    print(f"Part One")

    # Initial Position
    time = 0
    bus_ids = []
    # Get Instructions
    for line in open("sample_input1.txt", 'r').readlines():
        if not time:
            # get time
            time = int(line.strip('\n'))
        else:
            # get bus ids
            bus_list = line.split(',')
            for i in range(0, len(bus_list)):
                if bus_list[i] == 'x':
                    pass
                else:
                    bus_ids.append(int(bus_list[i]))

    print(time)
    print(bus_ids)

    later_time = time

    next = []

    for bus in bus_ids:
        while later_time % bus != 0:
            later_time += 1
        else:
            # print(f"Bus {bus} will arrive at {later_time}")
            arrival = {}
            arrival['bus_id'] = bus
            arrival['later_time'] = later_time
            next.append(arrival)
            later_time = time

    times = []
    for i in next:
        times.append(i['later_time'])

    next_departure = min(times)
    need_to_wait = next_departure - time

    for entry in next:
        if entry['later_time'] == next_departure:
            need_id = entry['bus_id']

    print(need_id * need_to_wait)

    print("Part Two")
    # 7,13,x,x,59,x,31,19
    # 0,1 ,x,x,4 ,x,5 ,6

    # 7,13,x,x,59,x,31,19
    for line in open("puzzle_input.txt", 'r').readlines():
        line = line.strip('\n')
        # print(line)

    remainders = []
    additions = []

    line = line.split(',')
    # print(line)

    for item in line:
        if item.isnumeric():
            remainders.append(item)

    diff = 0
    for item in line:
        if item.isnumeric():
            additions.append(diff)
            diff += 1
        else:
            diff += 1

    print("Remainders:", remainders)
    print("Additions:", additions)

    # System of Equations
    # WOLFRAM ALPHA
    # { Mod{t + addition[0], remainder[0]} == 0 , ... }
    # for all additions and remainders
