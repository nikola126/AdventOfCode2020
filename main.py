# Day 2

# Get Input
if __name__ == '__main__':

    pwd_list = []
    for line in open("puzzle_input.txt", "r"):
        line = line.strip('\n')
        pwd_list.append(line)

    # PART ONE

    entries = len(pwd_list)
    print(f"Report with {entries} entries")

    valid_passwords = 0
    # Loop through values
    for entry in pwd_list:
        # Get Password Policy
        entry = entry.split(' ')
        # Lower/Upper Count Limits
        indices = entry[0].split('-')
        lower = int(indices[0])
        upper = int(indices[1])
        # Character to look for
        char = entry[1].strip(':')
        # Password
        password = entry[2]

        # Info
        # print(f"{char} must be in {password} between {lower} and {upper} times ({password.count(char)}).")
        if lower <= password.count(char) <= upper:
            valid_passwords = valid_passwords + 1

    print(valid_passwords)

    # PART TWO
    valid_passwords = 0
    # Loop through values
    for entry in pwd_list:
        # Get Password Policy
        entry = entry.split(' ')
        # Get Position Indices
        indices = entry[0].split('-')
        index_one = int(indices[0])
        index_two = int(indices[1])
        # Character to look for
        char = entry[1].strip(':')
        # Password
        password = entry[2]
        # Get Letters at those Indices
        letter_one = password[index_one-1]
        letter_two = password[index_two-1]

        if (letter_one == char) ^ (letter_two == char):
            valid_passwords = valid_passwords + 1

    print(valid_passwords)




