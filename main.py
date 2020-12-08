# Day 5

if __name__ == '__main__':
    id_list = []

    # Get Input
    seats_read = 0
    for line in open("puzzle_input.txt", "r"):
        seats_read += 1
        # Analyze Line
        line = line.strip('\n')
        rows_string = line[:7]
        cols_string = line[7:]

        # Rows
        lower = 0
        upper = 127

        for letter in rows_string[:-1]:
            middle = round((upper - lower) / 2)
            if letter == 'F':
                upper = upper - middle
            else:
                lower = lower + middle
        # final character
        if rows_string[-1] == 'F':
            row = lower
        else:
            row = upper

        # Cols
        lower = 0
        upper = 7
        for letter in cols_string[:-1]:
            middle = round((upper - lower) / 2)
            if letter == 'L':
                upper = upper - middle
            else:
                lower = lower + middle
        # final character
        if cols_string[-1] == 'L':
            col = lower
        else:
            col = upper

        seat_id = row * 8 + col
        id_list.append(seat_id)

    print(f"Seats Read:{seats_read}\tIDs found:{len(id_list)}\tMax ID: {max(id_list)}")

    # PART TWO

    # sort id_list
    sorted_id_list = sorted(id_list)

    # read by twos
    arr_length = len(sorted_id_list)
    for i in range(0, arr_length-1):
        seat_left = sorted_id_list[i]
        seat_right = sorted_id_list[i + 1]
        if seat_right - seat_left == 1:
            pass
        else:
            print(sorted_id_list[i], sorted_id_list[i + 1])
            print("MISSING SEAT ID:", (sorted_id_list[i+1] + sorted_id_list[i])/2)
