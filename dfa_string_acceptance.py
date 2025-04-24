def dfa_string_acceptance(dfa, string):
    states, alphabet, transitions, start, final = dfa

    current_state = start
    for c in string:
        next_state = ""
        for transition in transitions:
            if transition[0] == current_state and c == transition[1]:
                next_state = transition[2]
                break
        if next_state == "":
            return False
        current_state = next_state

    if current_state in final:
        return True
    return False