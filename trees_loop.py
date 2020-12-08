def trees_loop(map,rows,cols,step_right,step_down):
    next_row = 0
    next_col = 0
    trees = 0
    while (next_row < rows):
        if (map[next_row][next_col] == 1):
            trees = trees + 1
        next_row = next_row + step_down
        next_col = next_col + step_right
        if (next_col >= cols):
            next_col = next_col - cols

    return trees