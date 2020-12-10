# Day 10

combinations = 0
route_set = set()
global route_count
route_count = 0
global walker_count
walker_count = 0
required_numbers = set()


def route_short_finder(data):
    for i in range(1, len(data) - 1):
        target = data[i]
        # print(f"Can i remove {target} and still reach the end?")
        shorter = data[:]
        shorter.remove(target)
        # print(f"Try this: {shorter}")

        if route_walker(shorter):
            # print("No")
            pass
        else:
            # print(f"No, {target} is a required number.")
            required_numbers.add(target)


def route_printer(data, idx):
    global combinations
    global walker_count
    go_ahead = True
    # print(data)
    for i in range(idx, len(data) - 1):
        target = data[i]
        # print(f"Can i remove {target} and still reach the end?")

        shorter = data[:]
        shorter.remove(target)
        # print(f"Shorter:{shorter}")
        # print(f"Required numbers:{required_numbers}")
        # print(f"Try this: {shorter}")
        # if all(elem in shorter for elem in required_numbers):
        #     # print("this may be ok", end=" ")
        #     pass
        # else:
        #     continue
        # print("Not all required numbers are in", end=" ")
        # go_ahead = False
        # pass
        # continue

        # faster if only 2 entries
        if len(shorter) == 2:
            return

        # if yes?
        if go_ahead:
            walker_count += 1
        if route_walker(shorter) and go_ahead:
            # try with even shorter path
            route_printer(shorter, i)
        else:
            pass
    return


def route_walker(way):
    global route_count
    # print("Way:",way)
    # if len(way) == 2:
    #     route_count += 1
    #     return True
    for j in range(0, len(way) - 1):
        if way[j + 1] - way[j] == 1 or way[j + 1] - way[j] == 2 or way[j + 1] - way[j] == 3:
            pass
        else:
            # print("No")
            return False
    # print("Yes")
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

    ways = [0] * len(data)
    # ways in which a connection to a previous adapter can be made
    ways[0] = ways[1] = 1
    if data[2] - data[0] <= 3:
        ways[2] = 2
    else:
        ways[2] = 1

    # starts 3 forward and looks up to 3 back
    # increments ways with the number of possible connections at each checked previous adapter
    for i in range(3, len(data)):
        for j in range(1, 4):
            # print("Looking at", data[i], "and", data[i - j], end="\t")
            if data[i] - data[i - j] <= 3:
                # print(f"Add {ways[i - j]} ways[{i} - {j}] at index {i}")
                ways[i] += ways[i - j]
            else:
                # print()
                pass

    # print(ways)
    # all possible combinations are at the last index
    print("Combinations:", ways[-1])
