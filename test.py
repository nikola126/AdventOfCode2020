fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def is_valid_passport(pp):
    for field in fields:
        if field not in pp:
            print(field)
            return False
    return True


with open('puzzle_input.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

valid_count = 0
all_count = 0

current_passport = ''
for line in data:
    if line != '':
        current_passport += ' ' + line
    else:
        if is_valid_passport(current_passport):
            valid_count += 1
            all_count += 1
        else:
            all_count += 1
        current_passport = ''

if is_valid_passport(current_passport):
    valid_count += 1

print(all_count)
print(valid_count)
print(all_count - valid_count)
