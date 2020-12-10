# Day 10


if __name__ == '__main__':

    print(f"Part One")
    # Get input
    data = []
    for line in open('puzzle_input.txt', 'r').readlines():
        line = line.strip('\n')
        data.append(int(line))

    start_voltage = 0
    i = 0
    reps = 0
    current_voltage = 0
    while True:
        target = current_voltage + 1
        print(f"Now:{current_voltage} Look for: {target}")
        if target not in data:
            pass
        elif target+3 not in data:
            break
        else:
            current_voltage = target
            target += 1


