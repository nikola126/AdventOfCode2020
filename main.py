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


if __name__ == '__main__':

    print(f"Part One")

    mask = ''
    cell = {'location': 0, 'value': 0}
    memory = []
    # Get Instructions
    for line in open("puzzle_input.txt", 'r').readlines():
        # Get Mask
        line = line.strip('\n')
        if 'mask' in line:
            mask = line[7:]
            # print("Updated mask:", mask)
        else:
            line = line.split('] = ')
            # get location
            loc = int(line[0][4:])
            # get value
            value = int(line[1])
            # value to binary
            binary = dec2bin(value, mask)
            # print("Binary:", binary)
            # apply mask
            masked = apply_mask(mask, binary)
            # print("After Mask:", binary)
            # value to decimal
            decimal = bin2dec(masked)
            # print("Save", decimal, "to", loc)
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


