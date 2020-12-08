# Day 3
import numpy as np
from trees_loop import trees_loop

# Get Input
if __name__ == '__main__':

    # Get Dimensions
    rows = 0
    cols = 0
    for line in open("puzzle_input.txt", "r"):
        line = line.strip('\n')
        cols = len(line)
        rows = rows + 1

    # Reshape map in array and populate with int values
    # Tree = # = 1
    # Open = . = 0
    # print(f"Map Dimensions: {x}x{y}")

    map = np.zeros((rows, cols))
    row = 0
    for line in open("puzzle_input.txt", "r"):
        line = line.strip('\n')
        for col in range(0, len(line)):
            if line[col] == '.':
                char = 0
            else:
                char = 1
            map[row][col] = int(char)
        row = row + 1
    print(map.shape)

    # Loop through the end ( THE MAP LOOPS TO THE RIGHT
    next_row = 0
    next_col = 0
    step_right = 3
    step_down = 1
    trees = 0
    # print(f"Rows:{rows}, Columns:{cols}")
    while (next_row < rows):
        # print(f"Go to Map[{next_row}][{next_col}] --> ", end=" ")
        # print(map[next_row][next_col])
        if (map[next_row][next_col] == 1):
            trees = trees + 1
        next_row = next_row + step_down
        next_col = next_col + step_right
        if (next_col >= cols):
            # print(f"Next col is {next_col} but max is {cols}. The new col should be {next_col - cols}")
            next_col = next_col - cols
    print(trees)

    # PART TWO
    print("PART TWO")

    trees_product = 1

    trees_product = trees_product * trees_loop(map, rows, cols, 1, 1)
    trees_product = trees_product * trees_loop(map, rows, cols, 3, 1)
    trees_product = trees_product * trees_loop(map, rows, cols, 5, 1)
    trees_product = trees_product * trees_loop(map, rows, cols, 7, 1)
    trees_product = trees_product * trees_loop(map, rows, cols, 1, 2)
    print(trees_product)
