# Day 14

def bin2dec(bin, mask_length):
    # gets string -> binary representation
    # returns int -> decimal representation
    # 1010
    bin_string = reversed(bin)
    power_multiplier = 0
    decimal = 0
    for idx in bin_string:
        add = int(idx) * (2**power_multiplier)
        decimal += add
        power_multiplier += 1

    return decimal

def dec2bin(dec, )





if __name__ == '__main__':

    print(f"Part One")

    mask_string = ''
    # Get Instructions
    for line in open("sample_input1.txt", 'r').readlines():
        # Get Mask
        line = line.strip('\n')
        if 'mask' in line:
            mask_string = line[7:]
        else:
            print(line)

    print("Mask:", mask_string, "Length:", len(mask_string))

    print(bin2dec('1001001', 36))
