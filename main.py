# Day 4
from analyze_field import *

if __name__ == '__main__':
    # Passport
    passport = {}
    passport['byr'] = None
    passport['iyr'] = None
    passport['eyr'] = None
    passport['hgt'] = None
    passport['hcl'] = None
    passport['ecl'] = None
    passport['pid'] = None
    # passport['cid'] = None

    invalid = 0
    in_file = 0
    # Get Input
    for line in open("puzzle_input.txt", "r"):
        line = line.strip('\n')
        if line == '':
            # EMPTY LINE REACHED
            in_file = in_file + 1
            # ANALYSE LAST PASSWORD
            for key in passport.keys():
                if passport[key] is None:
                    # print(key, invalid)
                    invalid = invalid + 1
                    break
            # RESET PASSPORT DATA
            for key in passport.keys():
                passport[key] = None
        else:
            # DATA REACHED
            # FILL PASSPORT DATA
            for key in passport.keys():
                if line.count(key):
                    passport[key] = 'Present'
                else:
                    pass
    # LAST LINE REACHED
    # FILL PASSPORT DATA
    in_file += 1
    for key in passport.keys():
        if line.count(key):
            passport[key] = 'Present'
        else:
            pass
    # ANALYSE LAST PASSPORT
    # print("Last passport:\n",passport)
    for key in passport.keys():
        if passport[key] is None:
            print(key, invalid)
            invalid = invalid + 1
            break

    print("All passports:", in_file)
    print("Valid passports:", in_file - invalid)
    print("Invalid passports:", invalid)

    # PART TWO
    print("PART TWO")
    in_file = 0
    invalid_part_two = 0
    invalid = False
    for key in passport.keys():
        passport[key] = None

    # Get Input
    for line in open("puzzle_input.txt", "r"):
        line = line.strip('\n')
        if line == '':
            in_file += 1
            # EMPTY LINE REACHED
            # ANALYSE LAST PASSWORD
            for key in passport.keys():
                if passport[key] != 'VALID':
                    # print(passport)
                    invalid = True
            if not invalid:
                # print("LAST PASSPORT WAS OK")
                pass
            else:
                invalid_part_two += 1
                # print("Invalid Passport", invalid_part_two)
            # RESET PASSPORT DATA
            # print("NEW PASSPORT")
            invalid = False
            for key in passport.keys():
                passport[key] = None
        else:
            # DATA REACHED
            # SPLIT BY FIELDS
            line = line.split(' ')
            # print(line)
            # ANALYZE FIELDS
            for item in line:
                field = item[0:3]
                value = item[4:]
                # print(f"Field [{field}] Value [{value}]")
                analyze_field(passport, field, value)
            # print(passport)
    # LAST LINE REACHED
    # print("Last line")
    in_file += 1
    # ANALYSE LAST PASSWORD
    for key in passport.keys():
        if passport[key] != 'VALID':
            invalid = True
    if not invalid:
        # print("LAST PASSPORT WAS OK")
        pass
    else:
        invalid_part_two += 1
        # print("Invalid Passport", invalid_part_two)
    # RESET PASSPORT DATA
    # print("NEW PASSPORT")
    invalid = False
    for key in passport.keys():
        passport[key] = None

    print("All passports:", in_file)
    print("Valid passports:", in_file - invalid_part_two)
    print("Invalid passports:", invalid_part_two)
