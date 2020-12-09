# Day 7

bags_checked = set()
bags_sum = 0


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


def bag_count(bags_list, bags_sum, current_bag, bags_inside, rec_level):
    print(f"Current Bag: {current_bag}")
    # get the data for the current bag
    for bag in bags_list:
        index = 0
        if current_bag['name'] == bag['name']:
            # if no sub_bags:
            if sum(current_bag['amounts']) == 0:
                print(f"No sub bag in {current_bag['name']}.")
                rec_level -= 1
                return 1
            else:
                # look in every sub_bag
                for sub_bag in bag['contains']:
                    for entry in bags_list:
                        if entry['name'] == sub_bag:
                            check_here = entry
                    # recursive call
                    bags_inside = bag['amounts'][index]
                    bags_below = bag_count(bags_list, bags_sum, check_here, bags_inside, rec_level + 1)
                    index += 1
    rec_level -= 1
    return 1


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

    # PART TWO TODO
    multiplier = 0
    for bag in bags_list:
        if target == bag['name']:
            result = bag_count(bags_list, bags_sum, bag, 1, 1)

    # print(result - 1)
