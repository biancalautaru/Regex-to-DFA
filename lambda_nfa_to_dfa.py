from queue import Queue

# dfs pentru lambda-miscari
def dfs(node, visited, transitions):
    visited.add(node)
    for (source, character, destination) in transitions:
        if source == node and character == "lambda" and destination not in visited:
            dfs(destination, visited, transitions)

def get_lambda_closures(states, transitions):
    lambda_closure = {}
    for state in states:
        visited = set()
        dfs(state, visited, transitions)
        lambda_closure[state] = visited
    return lambda_closure

def lambda_nfa_to_dfa(lambda_nfa):
    states, alphabet, transitions, start, final = lambda_nfa
    dfa_alphabet = alphabet - {"lambda"}

    lambda_closure = get_lambda_closures(states, transitions)

    new_start = frozenset(lambda_closure[start])
    new_states = {new_start}
    state_count = 0
    dfa_start = "q0"
    dfa_states = {new_start : dfa_start}
    dfa_transitions = set()

    queue = Queue()
    queue.put(new_start)
    while not queue.empty():
        current_state = queue.get()
        for c in dfa_alphabet:
            new_state = set()
            for state in current_state:
                for (source, character, destination) in transitions:
                    if source == state and character == c:
                        new_state |= lambda_closure[destination]

            if not new_state:
                continue

            next_state = frozenset(new_state)
            if next_state not in dfa_states:
                state_count += 1
                dfa_states[next_state] = f"q{state_count}"
                new_states.add(next_state)
                queue.put(next_state)

            dfa_transitions.add((dfa_states[current_state], c, dfa_states[next_state]))

    dfa_final = set()
    for states in new_states:
        for state in states:
            if state in final:
                dfa_final.add(dfa_states[states])
                break

    return (set(dfa_states.values()), dfa_alphabet, dfa_transitions, dfa_start, dfa_final)