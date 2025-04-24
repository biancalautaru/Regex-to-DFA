from lambda_nfa_utils import *

def get_alphabet(regex):
    alphabet = set()
    for c in regex:
        if c.isalnum():
            alphabet.add(c)
    return alphabet

# transforma un regex in forma postfixata intr-un lambda-nfa
def postfix_to_lambda_nfa(regex):
    alphabet = get_alphabet(regex) | {"lambda"}

    reset_states()
    stack = []
    for c in regex:
        part = ()
        if c in alphabet:
            part = litera(c, alphabet)
        elif c == "|":
            part = union(stack[-2], stack[-1])
            stack.pop(-1)
            stack.pop(-1)
        elif c == ".":
            part = concatenation(stack[-2], stack[-1])
            stack.pop(-1)
            stack.pop(-1)
        elif c == "*":
            part = star(stack[-1])
            stack.pop(-1)
        elif c == "+":
            part = plus(stack[-1])
            stack.pop(-1)
        elif c == "?":
            part = optional(stack[-1])
            stack.pop(-1)
        stack.append(part)

    return tuple(stack[0])