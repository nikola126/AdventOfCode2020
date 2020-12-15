# Day 15

if __name__ == '__main__':

    print(f"Part One")

    with open('puzzle_input.txt', 'r') as file:
        data = file.readlines()
        data = data[0].split(',')
        data = [int(num) for num in data]

        print(data)

        last_said = {}

        # add all values except the last one
        for step in range(0, len(data) - 1):
            num = data[step]
            last_said[num] = step
            # print(f"Step {i}: Say {num}.")

        for step in range(len(data) - 1, 2020):
            num = data[step]

            if num not in last_said:
                data.append(0)
                last_said[num] = step
                # print(f"Step {i}: {num} is not in memory. Say {num}.")
            else:
                j = last_said[num]
                new_num = step - j
                data.append(new_num)
                last_said[num] = step
                # print(f"Step {i}: {num} has been said. Add {i} - {j} to numbers. Say {num}.")

        print(data[-2])

        print("Part Two")
        last_said = {}

        # add all values except the last one
        for step in range(0, len(data) - 1):
            num = data[step]
            last_said[num] = step
            # print(f"Step {i}: Say {num}.")

        for step in range(len(data) - 1, 30000000):
            num = data[step]

            if num not in last_said:
                data.append(0)
                last_said[num] = step
                # print(f"Step {i}: {num} is not in memory. Say {num}.")
            else:
                j = last_said[num]
                new_num = step - j
                data.append(new_num)
                last_said[num] = step
                # print(f"Step {i}: {num} has been said. Add {i} - {j} to numbers. Say {num}.")

        print(data[-2])
