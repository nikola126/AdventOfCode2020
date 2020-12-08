def analyze_field(passport, field, value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if field == 'byr':
        if value.isdigit():
            if len(value) == 4:
                value = int(value)
                if 1920 <= value <= 2002:
                    passport[field] = 'VALID'
                else:
                    # print(field, value, '\t', 'byr (Birth Year) - four digits; at least 1920 and at most 2002.')
                    pass
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if field == 'iyr':
        if value.isdigit():
            if len(value) == 4:
                value = int(value)
                if 2010 <= value <= 2020:
                    passport[field] = 'VALID'
                else:
                    # print(field, value, '\t', 'iyr (Issue Year) - four digits; at least 2010 and at most 2020.')
                    pass
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if field == 'eyr':
        if value.isdigit():
            if len(value) == 4:
                value = int(value)
                if 2020 <= value <= 2030:
                    passport[field] = 'VALID'
                else:
                    # print(field, value, '\t', 'eyr (Expiration Year) - four digits; at least 2020 and at most 2030.')
                    pass
    # hgt (Height) - a number followed by either cm or in:
    if field == 'hgt':
        if len(value) >= 3:
            # print(value)
            units = value[-2:]
            height = int(value[:-2])
            if units == 'cm':
                # If cm, the number must be at least 150 and at most 193.
                if 150 <= height <= 193:
                    passport[field] = 'VALID'
                else:
                    # print(field, value, '\t', 'hgt (Height) - cm, the number must be at least 150 and at most 193.')
                    pass
            if units == 'in':
                # If in, the number must be at least 59 and at most 76.
                if 59 <= height <= 76:
                    passport[field] = 'VALID'
                else:
                    # print(field, value, '\t', 'hgt (Height) - in, the number must be at least 59 and at most 76.')
                    pass
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if field == 'hcl':
        # print(value)
        if value[0] == '#':
            if len(value[1:]) == 6:
                passport[field] = 'VALID'
            else:
                # print(field, value, '\t', 'hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.')
                pass
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    eye_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if field == 'ecl':
        if value in eye_values:
            passport[field] = 'VALID'
        else:
            # print(field, value, '\t', 'ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.')
            pass
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if field == 'pid':
        if len(value) == 9:
            # print(value)
            if value.isdigit():
                # print(value)
                passport[field] = 'VALID'
            else:
                # print(field, value, '\t', 'pid (Passport ID) - a nine-digit number, including leading zeroes.')
                pass
    # cid (Country ID) - ignored, missing or not.

    return True
