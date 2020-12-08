# Day 1

# Get Input
if __name__ == '__main__':

    report = []
    for line in open("puzzle_input.txt", "r"):
        line = line.strip('\n')
        line = int(line)
        report.append(line)

    entries = len(report)
    print(f"Report with {entries} entries:\n", report)

    # PART ONE
    # Loop Through Values
    offset = 1
    for entry_one in report:
        for entry_two in report[offset:]:
            sum = entry_one + entry_two
            if sum == 2020:
                result = entry_one * entry_two
                print(result)
        offset = offset + 1

    # PART TWO
    # Loop Through Values
    offset_one_initial = 1
    offset_two_initial = 2
    offset_one = 1
    offset_two = 2
    for entry_one in report:
        # print(f"Offsets: {offset_one}, {offset_two}")
        # print(f"Looking at {entry_one}")
        for entry_two in report[offset_one:]:
            # print(f"\tLooking at {entry_two}")
            for entry_three in report[offset_two:]:
                # print(f"\t\tLooking at {entry_three}")
                # print(f"\t\tLooking at {entry_one}, {entry_two} and {entry_three}")
                if (entry_one + entry_two + entry_three) == 2020:
                    result = (entry_one * entry_two * entry_three)
                    print(result)
            offset_two = offset_two + 1
        # Reset Offsets
        offset_one_initial = offset_one_initial + 1
        offset_two_initial = offset_two_initial + 1
        offset_one = offset_one_initial
        offset_two = offset_two_initial
