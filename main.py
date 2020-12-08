# Day 7

bags_checked = set()
bags_sum = 0
global operation_list
operation_list = []


def bag_check(bags_list, target, current_bag):
    if target in current_bag['contains']:
        bags_checked.add(current_bag['name'])
        print(current_bag['name'], sum(current_bag['amounts'][:]))
        return True
    else:
        # RECURSIVE CALL
        for bag in current_bag['contains']:
            if bag in bags_checked:
                bags_checked.add(current_bag['name'])
                print(current_bag['name'], sum(current_bag['amounts'][:]))
                return True
        if len(current_bag['contains']) == 0:
            return False
        else:
            for item in current_bag['contains']:
                # find the dictionary entry
                for entry in bags_list:
                    if entry['name'] == item:
                        check_here = entry
                if bag_check(bags_list, target, check_here):
                    bags_checked.add(current_bag['name'])
                    print(current_bag['name'], sum(current_bag['amounts'][:]))
                    return True


def bag_count(bags_list, bags_sum, current_bag, previous_number_of_bags):
    global operation_list

    print(f"Previous number of bags:", previous_number_of_bags)
    print(f"Current Bag: {current_bag['amounts']}")
    operation_list.append(current_bag['amounts'])
    operation_list.append(previous_number_of_bags)
    for bag in bags_list:
        index = 0
        if current_bag['name'] == bag['name']:
            # print(bag['contains'], bag['amounts'])
            for sub_bag in bag['contains']:
                # find the dictionary entry
                for entry in bags_list:
                    if entry['name'] == sub_bag:
                        check_here = entry
                    # recursive call
                # print("Recursive call:", bag['amounts'][index])
                previous_number_of_bags = bag['amounts'][index]
                bag_count(bags_list, bags_sum, check_here, previous_number_of_bags)
                index += 1
            # print("Going up")
            # operation_list.append('*')
            return


if __name__ == '__main__':

    # create list of dictionaries
    bags_list = []
    # light_red_bag = { inside: [bright_white, muted_yellow] max:[1 2] }
    for line in open('puzzle_input.txt', 'r').readlines():
        line = line.strip('\n')
        line = line.split(" ")
        name = line[0] + line[1]
        bag = {'name': name}
        # check for other bags inside
        if line[4] == 'no':
            bag['contains'] = []
            bag['amounts'] = [0]
        else:
            # isolate rest of the description
            description = line[4:]
            # how many inside ?
            bags_inside = len(description) / 4
            bag['contains'] = []
            bag['amounts'] = []
            for i in range(0, int(bags_inside)):
                bag_inside = description[1 + 4 * i] + description[2 + 4 * i]
                amount_inside = description[0 + 4 * i]
                bag['contains'].append(bag_inside)
                bag['amounts'].append(int(amount_inside))
        bags_list.append(bag)

    # for entry in bags_list:
    #     print(entry)

    target = 'shinygold'
    print(f"TARGET:", target)

    # check top level
    # for bag in bags_list:
    #     bag_check(bags_list, target, bag)
    #
    # print("SET:", set(bags_checked))
    # print("LENGTH:", len(set(bags_checked)))

    # PART TWO
    multiplier = 0
    for bag in bags_list:
        if target == bag['name']:
            bag_count(bags_list, bags_sum, bag, 1)

    print(operation_list)
    correct_operation_list = []
    for step in operation_list:
        if type(step) is list:
            correct_operation_list.append(sum(step))
        else:
            correct_operation_list.append(step)
    correct_operation_list.reverse()
    print(correct_operation_list)

    result = 0
    action = '+'
    #
    for i in range(0, len(correct_operation_list) - 1, 2):
        print(correct_operation_list[i], correct_operation_list[i + 1], 'sum:',
              correct_operation_list[i] + correct_operation_list[i + 1])

    # print('(((((2*2+2)*2+2)*2+2)*2+2)*2+2)*1')
    # print(result)
