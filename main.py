from regex_utils import shunting_yard
from postfix_to_lambda_nfa import postfix_to_lambda_nfa
from lambda_nfa_to_dfa import lambda_nfa_to_dfa
from dfa_string_acceptance import dfa_string_acceptance

def dfa(regex):
    return lambda_nfa_to_dfa(postfix_to_lambda_nfa(shunting_yard(regex)))

if __name__ == "__main__":
    import json
    f = open("tests.json", "r")
    tests = json.loads(f.read())
    f.close()

    g = open("results.txt", "w")
    ok = True
    for test in tests:
        name = test["name"]
        regex = test["regex"]
        test_strings = test["test_strings"]
        g.write(f"{name} -> {regex}\n")
        for test_string in test_strings:
            input = test_string["input"]
            expected = test_string["expected"]
            actual = dfa_string_acceptance(dfa(regex), input)
            g.write(f"    {input} -> expected: {expected}, actual: {actual}\n")
            if actual != expected:
                ok = False
        g.write("\n")

    if ok == True:
        g.write("All tests passed!")
    else:
        g.write("Some tests failed!")