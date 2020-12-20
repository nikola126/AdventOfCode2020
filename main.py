# Day 18

def evaluator(exp):
    # operators have same precedence
    # evaluated left to right
    # returns a shortened expression
    eval = []
    for i in range(0, len(exp) - 1):
        if exp[i] == '+':
            result = exp[i - 1] + exp[i + 1]
            eval.append(result)
            for j in range(i + 2, len(exp)):
                eval.append(exp[j])
            break
        if exp[i] == '*':
            result = exp[i - 1] * exp[i + 1]
            eval.append(result)
            for j in range(i + 2, len(exp)):
                eval.append(exp[j])
            break
    # print("Evaluator:", eval)
    return eval


def parentheses(exp):
    # looks for a closing parentheses
    # evaluates everything inside
    # returns a shortened expression
    eval = []
    open_idx = 0
    closing_idx = 0
    for i in range(0, len(exp)):
        # remember the index of the last opening parentheses
        # print("Now checking", exp[i])
        if exp[i] == '(':
            open_idx = i
        if exp[i] == ')':
            closing_idx = i
            inside = exp[open_idx + 1:i]
            break
    # print("Before while:", inside)
    while len(inside) != 1:
        inside = evaluator(inside)
    # print("Inside parentheses:", inside)

    shortened = exp[0:open_idx] + list(inside) + exp[closing_idx + 1:]
    # print("Shortened:", shortened)
    return shortened


if __name__ == '__main__':

    print(f"Part One")
    results = []
    # Get Expressions
    for line in open("puzzle_input.txt", 'r').readlines():
        line = line.strip('\n')
        # print("Line:", line)
        # split to individual characters
        expression = []
        for char in line:
            if char == ' ':
                pass
            else:
                expression.append(char)
        # convert digits to ints
        for i in range(0, len(expression)):
            if expression[i].isdigit():
                expression[i] = int(expression[i])
        # print("Expression:", expression)

        # remove parentheses
        while '(' in expression:
            expression = parentheses(expression)
        # print("Expression after removing parentheses:", expression)

        # calculate the rest
        while len(expression) != 1:
            expression = evaluator(expression)
        print("RESULT ->", expression)
        results.append(expression[0])

    print("Sum of results:", sum(results))