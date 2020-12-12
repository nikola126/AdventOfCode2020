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


def move_ship_and_waypoint():
    pass


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
        if code == 'R' or code == 'L':
            # Change rotation
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

    print(f"Part Two")
    # Initial Positions
    ship_x = 0
    ship_y = 0
    way_x = 10
    way_y = 1

    # Get Instructions
    for line in open("puzzle_input.txt", 'r').readlines():
        line = line.strip('\n')
        # Read Instruction
        code = line[0]
        number = int(line[1:])
        print(f"Ship [{ship_x}][{ship_y}]\t", f"Waypoint[{way_x}][{way_y}]")
        if code == 'R' or code == 'L':
            # Rotate Waypoint Around Ship
            if code == 'R':
                degrees = number
                # remove 90 degrees and change rotation + 1
                while degrees:
                    # Remember relative values
                    rel_x = way_x - ship_x
                    rel_y = way_y - ship_y
                    # print("Rotate R")
                    degrees -= 90
                    new_x = rel_y
                    new_y = rel_x * -1
                    # apply
                    way_x = ship_x + new_x
                    way_y = ship_y + new_y
            if code == 'L':
                degrees = number
                # remove 90 degrees and change rotation + 1
                while degrees:
                    # Remember relative values
                    rel_x = way_x - ship_x
                    rel_y = way_y - ship_y
                    # print("Rotate L")
                    degrees -= 90
                    new_x = rel_y * -1
                    new_y = rel_x
                    # apply
                    way_x = ship_x + new_x
                    way_y = ship_y + new_y
        else:
            # Move in Specific Direction
            if code == 'F':
                # Remember relative values
                rel_x = way_x - ship_x
                rel_y = way_y - ship_y
                # Move ship to waypoint
                ship_x += number * rel_x
                ship_y += number * rel_y
                # Move waypoint with ship
                way_x = ship_x + rel_x
                way_y = ship_y + rel_y
            if code == 'N':
                # Move waypoint
                way_y += number
            if code == 'E':
                # Move waypoint
                way_x += number
            if code == 'S':
                # Move waypoint
                way_y -= number
                pass
            if code == 'W':
                # Move waypoint
                way_x -= number
        # print(line)

    print(f"Ship [{ship_x}][{ship_y}]\t", f"Waypoint[{way_x}][{way_y}]")
    print(f"Manhattan Distance:{abs(ship_x) + abs(ship_y)}")
