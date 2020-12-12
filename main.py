# Day 12

if __name__ == '__main__':

    print(f"Part One")

    # Initial Position
    pos_x = 0
    pos_y = 0
    # Get Instructions
    for line in open("sample_input1.txt", 'r').readlines():
        line = line.strip('\n')
        code = line[0]
        number = int(line[1:])
        print(f"Code: {code} Number: {number}")

