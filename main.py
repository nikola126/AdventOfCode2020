# Day 6

if __name__ == '__main__':

    unique_questions = {}
    unique_answers = 0
    for line in open('puzzle_input.txt', 'r').readlines():
        line = line.strip('\n')
        if line == '':
            # new group, count the unique answers and reset dictionary
            unique_answers += len(unique_questions.keys())
            unique_questions = {}
        else:
            for char in line:
                # add unique answers to dictionary
                if char not in unique_questions.keys():
                    unique_questions[char] = 1
                else:
                    pass
    # check last line
    unique_answers += len(unique_questions.keys())
    unique_questions = {}

    print(unique_answers)

    # PART TWO
    print("PART TWO")
    answers = {}
    everyone = 0

    people = 0
    for line in open('puzzle_input.txt', 'r').readlines():
        line = line.strip('\n')
        if line == '':
            # new group
            print(f"Questions to which all {people} people answered:")
            for key in answers.keys():
                if answers[key] == people:
                    print(key)
                    everyone += 1
            people = 0
            answers = {}
        else:
            people += 1
            for char in line:
                # add unique answers to dictionary
                if char not in answers.keys():
                    answers[char] = 1
                else:
                    answers[char] += 1

    # check last line
    print(f"Questions to which all {people} people answered:")
    for key in answers.keys():
        if answers[key] == people:
            print(key)
            everyone += 1

    print(everyone)