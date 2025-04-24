# adauga .
def get_complete_regex(input):
    regex = input[0]
    for i in range(1, len(input)):
        if (input[i].isalnum() or input[i] == "(") and input[i - 1] not in "(|":
            regex += "."
        regex += input[i]
    return regex

def shunting_yard(input):
    regex = get_complete_regex(input)

    # transforma regexul in forma postfixata
    precedence = {"|": 1, ".": 2, "*": 3, "+": 3, "?": 4}
    output = []
    stack = []
    for c in regex:
        if c.isalnum():
            output.append(c)
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while len(stack) > 0 and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while len(stack) > 0 and stack[-1] != "(" and precedence[c] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(c)
    while len(stack) > 0:
        output.append(stack.pop())

    return output