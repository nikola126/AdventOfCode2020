# Day 16

if __name__ == '__main__':

    print(f"Part One")

    your_ticket_reached = False
    nearby_tickets_reached = False
    fields = {}
    ticket_error_rate = 0
    my_ticket = []
    # Get Instructions
    for line in open("puzzle_input.txt", 'r').readlines():
        line = line.strip('\n')
        if len(line) == 0:
            # empty line
            pass
        else:
            if '-' in line:
                # field_name and ranges
                line = line.split(':')
                field_name = line[0]
                # ranges
                ranges_field = line[1]
                ranges_field = ranges_field.split(' ')
                first_range = ranges_field[1]
                second_range = ranges_field[3]
                first_range = first_range.split('-')
                second_range = second_range.split('-')
                ranges = []
                for i in range(int(first_range[0]), int(first_range[1]) + 1):
                    ranges.append(i)
                for i in range(int(second_range[0]), int(second_range[1]) + 1):
                    ranges.append(i)
                # add valid values to dictionary
                fields[field_name] = ranges
            if 'your' in line:
                your_ticket_reached = True
                continue
            if your_ticket_reached:
                line = line.split(',')
                your_ticket = line
                your_ticket_reached = False
                # save information about my ticket
                for item in your_ticket:
                    my_ticket.append(int(item))
            if 'nearby' in line:
                nearby_tickets_reached = True
                continue
            if nearby_tickets_reached:
                line = line.split(',')
                # convert to ints
                for i in range(0, len(line)):
                    line[i] = int(line[i])
                # check if its in any range
                incorrect = []
                for item in line:
                    for field in fields:
                        if item in fields[field]:
                            # remove from list
                            if item in incorrect:
                                incorrect.remove(item)
                            break
                        else:
                            # add to list of incorrect values
                            if item not in incorrect:
                                incorrect.append(item)
                            pass
                # add to the error rate
                ticket_error_rate += sum(incorrect)
    print("Fields and Ranges:")
    for field in fields:
        print(field)
    print("My ticket:", my_ticket)
    print("Ticket Error Rate:", ticket_error_rate)

    print("Part Two")


