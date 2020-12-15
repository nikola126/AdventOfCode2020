# Day 14

def bin2dec(bin):
    # gets string -> binary representation
    # returns int -> decimal representation
    # 1010
    bin_string = reversed(bin)
    power_multiplier = 0
    decimal = 0
    for idx in bin_string:
        add = int(idx) * (2 ** power_multiplier)
        decimal += add
        power_multiplier += 1

    return decimal


def dec2bin(dec, mask):
    bin = []
    while dec != 0:
        bin.append(dec % 2)
        dec = dec // 2
    # append zeros to fill to mask
    while len(bin) < len(mask):
        bin.append(0)
    # reverse
    bin.reverse()
    return bin


def apply_mask(mask, bin):
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            pass
        elif mask[i] == '0':
            bin[i] = 0
        else:
            bin[i] = 1
    return bin


def apply_mask_2(mask, bin):
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            bin[i] = 'X'
        elif mask[i] == '0':
            pass
        else:
            bin[i] = 1
    return bin


def get_addresses(masked_s):
    # base case
    if 'X' not in masked_s:
        return masked_s

    addresses = ''
    x_idx = int(masked_s.index('X'))
    with0 = masked_s[:x_idx] + '0' + masked_s[x_idx + 1:]
    with1 = masked_s[:x_idx] + '1' + masked_s[x_idx + 1:]

    addresses += get_addresses(with0) + ','
    addresses += get_addresses(with1)

    return addresses


if __name__ == '__main__':

    print(f"Part One")

    mask = ''
    cell = {'location': 0, 'value': 0}
    memory = []
    lines_passed = 0
    # Get Instructions
    for line in open("puzzle_input.txt", 'r').readlines():
        # Get Mask
        line = line.strip('\n')
        if 'mask' in line:
            mask = line[7:]
        else:
            line = line.split('] = ')
            # get location
            loc = int(line[0][4:])
            # get value
            value = int(line[1])
            # value to binary
            binary = dec2bin(value, mask)
            # apply mask
            masked = apply_mask(mask, binary)
            # value to decimal
            decimal = bin2dec(masked)
            # save value in cell in memory
            saved = False
            for cel in memory:
                if cel['location'] == loc:
                    cel['value'] = decimal
                    saved = True
                    break
            if not saved:
                cell = {'location': loc, 'value': decimal}
                memory.append(cell)

    total = 0
    for cel in memory:
        total += cel['value']

    print(total)

    print("Part Two")

    memory = []
    # Get Instructions
    for line in open("puzzle_input.txt", 'r').readlines():
        lines_passed += 1
        print("Now at line", lines_passed)
        # Get Mask
        line = line.strip('\n')
        if 'mask' in line:
            mask = line[7:]
        else:
            line = line.split('] = ')
            # get location
            loc = int(line[0][4:])
            # get value
            value = int(line[1])
            # loc to binary!!!
            binary = dec2bin(loc, mask)
            # apply mask
            masked = apply_mask_2(mask, binary)
            # convert to string
            masked_string = ""
            masked_string = masked_string.join([str(elem) for elem in masked])
            # get all possible addresses (as a string with commas)
            addresses_to_visit = get_addresses(masked_string)
            # split at commas
            addresses_to_visit = addresses_to_visit.split(',')
            # convert addresses to decimal
            loc_list = []
            for add in addresses_to_visit:
                loc_list.append(bin2dec(add))
            # go at every address and save value there
            for loc in loc_list:
                # save value in cell in memory
                saved = False
                for cel in memory:
                    if cel['location'] == loc:
                        cel['value'] = value
                        saved = True
                        break
                if not saved:
                    cell = {'location': loc, 'value': value}
                    memory.append(cell)

    total = 0
    for cel in memory:
        total += cel['value']

    print(total)
