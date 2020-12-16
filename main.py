# Day 16

def check_validity(line, fields):
    # returns the sum of incorrect values
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
    return sum(incorrect)


def check_validity_part_two(line, fields):
    # returns True if the ticket is valid
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
    if sum(incorrect) == 0:
        return True
    else:
        # print("invalid ticket", incorrect)
        return False


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
                # add to the error rate
                ticket_error_rate += check_validity(line, fields)

    # print("Fields and Ranges:")
    # for field in fields:
    #     print(field)
    print("My ticket:", my_ticket)
    print("Ticket Error Rate:", ticket_error_rate)

    print("Part Two")
    your_ticket_reached = False
    nearby_tickets_reached = False
    fields = {}
    ticket_error_rate = 0
    my_ticket = []
    fields_count = 0
    column_check = {}
    valid_tickets = 0
    invalid_tickets = 0
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
                fields_count += 1
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
                print("Tickets have", fields_count, "categories")
                # create several lists to which values for each category will be appended
                for i in range(fields_count):
                    column_check[i] = []
                # print(column_check)
                nearby_tickets_reached = True
                continue
            if nearby_tickets_reached:
                line = line.split(',')
                # convert to ints
                for i in range(0, len(line)):
                    line[i] = int(line[i])
                # check if valid
                if check_validity_part_two(line, fields):
                    valid_tickets += 1
                    # print("This ticket is valid")
                    for i in range(0, fields_count):
                        # print("Add", line[i], "to field", i)
                        column_check[i].append(line[i])
                else:
                    # print("Invalid ticket, ignore it")
                    invalid_tickets += 1
                    pass

    # print("Values Check:", column_check)
    # print("Fields:", fields)
    print("Valid Tickets:", valid_tickets)
    print("Invalid Tickets:", invalid_tickets)
    for i in range(fields_count):
        # print("Now checking position", i)
        required_inside = len(column_check[i])
        inside = 0
        # print("Required inside a single range:", required_inside)
        for field in fields:
            for value in column_check[i]:
                # print("Check if", value, "is in", field)
                if value in fields[field]:
                    inside += 1
                    # print("It is!")
            # print("values in range of position", field, ":", inside)
            if inside == required_inside:
                print("Position", i, "corresponds to", field,"your ticket:",my_ticket[i])
                fields.pop(field)
                inside = 0
                break
            else:
                # print("Inconclusive, resetting")
                inside = 0
                # break

    # 2 4 5 7 8 9
    # 59 * 151 * 107 * 73 * 109 * 157
    # print("Fields Left:")
    # for field in fields:
    #     print(field)
    # print("My ticket:", my_ticket)
