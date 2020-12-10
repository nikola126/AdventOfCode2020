# Day 9


if __name__ == '__main__':

    print(f"Part One")
    # Get input
    transmission = []
    for line in open('puzzle_input.txt', 'r').readlines():
        transmission.append(int(line))

    # Loop through
    preamble_length = 25
    preamble = []

    for i in range(preamble_length - 1, len(transmission)):
        preamble = transmission[i - preamble_length:i]
        check = transmission[i]
        # Look for Sums
        if len(preamble) == preamble_length:
            valid_found = 0
            for i in range(0, len(preamble)):
                for j in range(i + 1, len(preamble)):
                    if preamble[i] + preamble[j] == check:
                        valid_found += 1
            if valid_found == 0:
                break

    print("Found invalid number:", check)

    print(f"Part Two")
    # Loop through
    preamble_length = 25
    preamble = []

    for i in range(preamble_length - 1, len(transmission)):
        preamble = transmission[i - preamble_length:i]
        check = transmission[i]
        # Look for Sums
        if len(preamble) == preamble_length:
            valid_found = 0
            for i in range(0, len(preamble)):
                for j in range(i + 1, len(preamble)):
                    if preamble[i] + preamble[j] == check:
                        valid_found += 1
            if valid_found == 0:
                break

    print("Invalid number:", check)

    # find contiguous set of numbers which sum to our number
    sum = 0
    values_in_sum = []
    i = 0
    start_loc = 0
    while True:
        sum += transmission[i]
        values_in_sum.append(transmission[i])
        # print(f"Sum:{sum} Values in Sum: {values_in_sum}")
        if sum == check:
            break
        if sum > check:
            # empty sum and buffer, start over
            sum = 0
            values_in_sum = []
            start_loc += 1
            i = start_loc
        else:
            i += 1
    print(f"Check: {check} Sum: {sum} Values in Sum: {values_in_sum}")

    print(f"Result: {max(values_in_sum) + min(values_in_sum)}")


