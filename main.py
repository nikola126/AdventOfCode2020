# Day 11

def get_seated(grid, max_row, max_col, changes, x, y):
    # print(f"Now at coordinates [{x}][{y}]")
    occupied_around = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            # Check if out of grid
            # print(f"Look at [{i}][{j}]", end='')
            if i < 0 or i >= max_row or j < 0 or j >= max_col or (i == x and j == y):
                # print(f"[{i}][{j}] is invalid")
                # Invalid Position
                pass
            else:
                # check current location status
                if grid[i][j] == '.':
                    pass
                if grid[i][j] == '#':
                    occupied_around += 1
                if grid[i][j] == 'L':
                    pass

    # print(f"Occupied around:{occupied_around}")
    if occupied_around == 0 and grid[x][y] == 'L':
        # print(f"Change [{x}][{y}] to #")
        changes.append(x)
        changes.append(y)

    return changes


def stand_up(grid, max_row, max_col, changes, x, y):
    # print(f"Now at coordinates [{x}][{y}]")
    occupied_around = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            # Check if out of grid
            # print(f"Look at [{i}][{j}]", end='')
            if i < 0 or i >= max_row or j < 0 or j >= max_col or (i == x and j == y):
                # print(f"[{i}][{j}] is invalid")
                # Invalid Position
                pass
            else:
                # check current location status
                if grid[i][j] == '.':
                    pass
                if grid[i][j] == '#':
                    occupied_around += 1
                if grid[i][j] == 'L':
                    pass

    # print(f"Occupied around:{occupied_around}")
    if occupied_around >= 4 and grid[x][y] == '#':
        # print(f"Change [{x}][{y}] to #")
        changes.append(x)
        changes.append(y)

    return changes


def get_seated_2(grid, max_row, max_col, changes, x, y):
    # print(f"Now at coordinates [{x}][{y}]")
    occupied_around = 0

    # Look in depth in all 8 directions
    i = x
    j = y
    in_grid = True
    # UP
    while True:
        j += 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DOWN
    while True:
        j -= 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # LEFT
    while True:
        i -= 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # RIGHT
    while True:
        i += 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DIAGONAL UL
    while True:
        i -= 1
        j -= 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DIAGONAL UR
    while True:
        i += 1
        j -= 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DIAGONAL DL
    while True:
        i -= 1
        j += 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DIAGONAL DR
    while True:
        i += 1
        j += 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # print(f"Occupied around:{occupied_around}")
    if occupied_around == 0 and grid[x][y] == 'L':
        # print(f"Change [{x}][{y}] to #")
        changes.append(x)
        changes.append(y)

    return changes


def stand_up_2(grid, max_row, max_col, changes, x, y):
    # print(f"Now at coordinates [{x}][{y}]")
    occupied_around = 0

    # Look in depth in all 8 directions
    i = x
    j = y
    in_grid = True
    # UP
    while True:
        j += 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DOWN
    while True:
        j -= 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # LEFT
    while True:
        i -= 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # RIGHT
    while True:
        i += 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DIAGONAL UL
    while True:
        i -= 1
        j -= 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DIAGONAL UR
    while True:
        i += 1
        j -= 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DIAGONAL DL
    while True:
        i -= 1
        j += 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # DIAGONAL DR
    while True:
        i += 1
        j += 1
        # Check if out of bounds
        if i < 0 or i >= max_row or j < 0 or j >= max_col:
            break
        # Look for an occupied seat, break when one is found
        if grid[i][j] == '#':
            # print(f"Found an occupied seat at [{i}][{j}]")
            occupied_around += 1
            break
        # If an empty seat is found, break too
        if grid[i][j] == 'L':
            break
    i = x
    j = y
    # print(f"Occupied around:{occupied_around}")
    if occupied_around >= 5 and grid[x][y] == '#':
        # print(f"Change [{x}][{y}] to #")
        changes.append(x)
        changes.append(y)

    return changes


if __name__ == '__main__':

    print(f"Part One")

    # Sizes
    rows = 0
    cols = 0

    # Get Input
    layout = []
    rows = 0
    for line in open("puzzle_input.txt", 'r').readlines():
        line = list(line.strip('\n'))
        layout.append(line)
        rows += 1
        cols = len(line)

    # for row in layout:
    #     for place in row:
    #         print(place, end='')
    #     print()
    print(f"Grid [{rows} x {cols}]")

    changes = 1
    cycles = 0

    while changes != 0:
        # Start Cycle --------------------------------------------------------------------
        # Sit Down -----------------------------------------------------------------------
        changelog = []
        for i in range(0, rows):
            for j in range(0, cols):
                changelog = get_seated(layout, rows, cols, changelog, i, j)

        # Apply changes
        for i in range(0, len(changelog), 2):
            layout[changelog[i]][changelog[i + 1]] = '#'

        # for row in layout:
        #     print(row)
        # print(f"Changes:{len(changelog) / 2}")

        changes = len(changelog) / 2
        cycles += 1
        if changes == 0:
            break

        # Stand Up -----------------------------------------------------------------------
        changelog = []
        for i in range(0, rows):
            for j in range(0, cols):
                changelog = stand_up(layout, rows, cols, changelog, i, j)

        # Apply changes
        for i in range(0, len(changelog), 2):
            layout[changelog[i]][changelog[i + 1]] = 'L'

        # for row in layout:
        #     print(row)
        # print(f"Changes:{len(changelog) / 2}")

        changes = len(changelog) / 2
        cycles += 1
        if changes == 0:
            break
        # End Cycle -----------------------------------------------------------------------

    print("Cycles:", cycles - 1)

    # Count Occupied
    occupied = 0
    for row in layout:
        for place in row:
            if place == '#':
                occupied += 1
    print("Occupied:", occupied)

    print("Part Two")

    # Get Input
    layout = []
    rows = 0
    for line in open("puzzle_input.txt", 'r').readlines():
        line = list(line.strip('\n'))
        layout.append(line)
        rows += 1
        cols = len(line)

    occupied = 0
    changes = 1
    cycles = 0

    while changes != 0:
        # Start Cycle --------------------------------------------------------------------
        # Sit Down -----------------------------------------------------------------------
        changelog = []
        for i in range(0, rows):
            for j in range(0, cols):
                changelog = get_seated_2(layout, rows, cols, changelog, i, j)

        # Apply changes
        for i in range(0, len(changelog), 2):
            layout[changelog[i]][changelog[i + 1]] = '#'

        # for row in layout:
        #     print(row)
        # print(f"Changes:{len(changelog) / 2}")

        changes = len(changelog) / 2
        cycles += 1
        if changes == 0:
            break

        # Stand Up -----------------------------------------------------------------------
        changelog = []
        for i in range(0, rows):
            for j in range(0, cols):
                changelog = stand_up_2(layout, rows, cols, changelog, i, j)

        # Apply changes
        for i in range(0, len(changelog), 2):
            layout[changelog[i]][changelog[i + 1]] = 'L'

        # for row in layout:
        #     print(row)
        # print(f"Changes:{len(changelog) / 2}")

        changes = len(changelog) / 2
        cycles += 1
        if changes == 0:
            break
        # End Cycle -----------------------------------------------------------------------

    print("Cycles:", cycles - 1)

    # Count Occupied
    occupied = 0
    for row in layout:
        for place in row:
            if place == '#':
                occupied += 1
    print("Occupied:", occupied)
