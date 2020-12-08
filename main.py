# Day 3

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
            # ANALYSE LAST PASSWORD
            for key in passport.keys():
                if passport[key] is None:
                    invalid = invalid + 1
                    print(key, invalid)
                    break
            # RESET PASSPORT DATA
            in_file = in_file + 1
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
    for key in passport.keys():
        if line.count(key):
            passport[key] = 'Present'
        else:
            pass
    # ANALYSE LAST PASSPORT
    # print("Last passport:\n",passport)
    for key in passport.keys():
        if passport[key] is None:
            invalid = invalid + 1
            print(key, invalid)
            break

    print("All passports:", in_file)
    print("Valid passports:", in_file - invalid)
    print("Invalid passports:", invalid)

