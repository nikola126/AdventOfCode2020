# Day 12

def move_forward(x, y, rotation, mov):
    # N E S W
    # 1 2 3 4
    if rotation == 1:
        y += mov
    if rotation == 2:
        x += mov
    if rotation == 3:
        y -= mov
    if rotation == 4:
        x -= mov

    return x, y


if __name__ == '__main__':

    print(f"Part One")

    # Initial Position
    pos_x = 0
    pos_y = 0
    # N E S W
    # 1 2 3 4
    ori = 2
    # Get Instructions
    for line in open("puzzle_input.txt", 'r').readlines():
        line = line.strip('\n')
        # Read Instruction
        code = line[0]
        number = int(line[1:])
        # print(f"Command: [{code}][{number}] Orientation:", ori)
        # Change rotation
        if code == 'R' or code == 'L':
            if code == 'R':
                degrees = number
                # remove 90 degrees and change rotation + 1
                # N E S W
                # 1 2 3 4
                while degrees:
                    degrees -= 90
                    ori += 1
                    if ori > 4:
                        ori -= 4
                    if ori < 1:
                        ori += 4
            if code == 'L':
                degrees = number
                # remove 90 degrees and change rotation - 1
                # N E S W
                # 1 2 3 4
                while degrees:
                    degrees -= 90
                    ori -= 1
                    if ori > 4:
                        ori -= 4
                    if ori < 1:
                        ori += 4
        else:
            # Move in Specific Direction
            if code == 'F':
                # use previous rotation
                # print("Forward with orientation", ori)
                pos_x, pos_y = move_forward(pos_x, pos_y, ori, number)
            # N E S W
            # 1 2 3 4
            if code == 'N':
                pos_x, pos_y = move_forward(pos_x, pos_y, 1, number)
            if code == 'E':
                pos_x, pos_y = move_forward(pos_x, pos_y, 2, number)
            if code == 'S':
                pos_x, pos_y = move_forward(pos_x, pos_y, 3, number)
            if code == 'W':
                pos_x, pos_y = move_forward(pos_x, pos_y, 4, number)
        # print(f"Ship now at: [{pos_x}][{pos_y}]")

    print(f"Final: [{pos_x}][{pos_y}]")
    print(f"Manhattan Distance:{abs(pos_x) + abs(pos_y)}")
