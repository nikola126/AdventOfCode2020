# Day 10

combinations = 0
route_set = set()
global route_count
route_count = 0


def route_printer(data, idx):
    global combinations
    # print(data)
    for i in range(idx, len(data) - 1):
        target = data[i]
        # print(f"Can i remove {target} and still reach the end?")
        shorter = data[:]
        shorter.remove(target)
        # print(shorter)
        # if yes?
        if route_walker(shorter):
            # try with even shorter path
            route_printer(shorter, i)
    return


def route_walker(way):
    global route_count
    # print("Way:",way)
    for j in range(0, len(way) - 1):
        if way[j + 1] - way[j] == 1 or way[j + 1] - way[j] == 2 or way[j + 1] - way[j] == 3:
            pass
        else:
            # print("No")
            return False
    # print("Yes -> Valid Route:", way)
    # route_set.add(tuple(way))
    route_count += 1
    return True


if __name__ == '__main__':

    print(f"Part One")
    # Get input
    # Append outlet voltage (0)
    data = [0]
    for line in open('puzzle_input.txt', 'r').readlines():
        line = line.strip('\n')
        data.append(int(line))

    # Append device adapter (max + 3)
    data.append(max(data) + 3)

    # Sort Data
    data = sorted(data)

    diff_1 = 0
    diff_3 = 0

    for i in range(0, len(data) - 1):
        # print(f"Looking at {data[i]} and {data[i+1]}")
        if data[i + 1] - data[i] == 1:
            diff_1 += 1
            # print(f"Difference of 1 between {data[i]} and {data[i+1]}")
        elif data[i + 1] - data[i] == 3:
            # print(f"Difference of 3 between {data[i]} and {data[i+1]}")
            diff_3 += 1

    print(f"Diff 1: {diff_1}, Diff 3: {diff_3}")
    print(f"Result: {diff_1 * diff_3}")

    print("PART TWO")
    # print(data)
    route_printer(data, 1)
    # print(combinations + 1)
    # print(route_set)
    # print(len(route_set) + 1)
    print(route_count)
