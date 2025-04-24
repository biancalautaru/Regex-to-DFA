from itertools import count

state_counter = count()

def reset_states():
    global state_counter
    state_counter = count()

# returneaza o stare noua, care nu exista
def new_state():
    return f"q{next(state_counter)}"

# cazul 1: e = multimea vida
def multimea_vida(alphabet):
    start = new_state()
    return ({start}, alphabet, set(), start, set())

# cazul 2: e = cuvantul vid (lambda)
def cuvantul_vid(alphabet):
    start = new_state()
    return ({start}, alphabet, set(), start, {start})

# cazul 3: e = o litera din alfabet
def litera(character, alphabet):
    start = new_state()
    final = new_state()
    return ({start, final}, alphabet, {(start, character, final)}, start, {final})

# cazul 4: e = e1 | e2
def union(e1, e2):
    states1, alphabet1, transitions1, start1, final1 = e1
    states2, alphabet2, transitions2, start2, final2 = e2

    states = states1 | states2
    start = new_state()
    final = new_state()
    states.add(start)
    states.add(final)

    transitions = transitions1 | transitions2
    transitions.add((start, "lambda", start1))
    transitions.add((start, "lambda", start2))
    for f in final1:
        transitions.add((f, "lambda", final))
    for f in final2:
        transitions.add((f, "lambda", final))

    return (states, alphabet1 | alphabet2, transitions, start, {final})

# cazul 5: e = e1 . e2
def concatenation(e1, e2):
    states1, alphabet1, transitions1, start1, final1 = e1
    states2, alphabet2, transitions2, start2, final2 = e2

    transitions = transitions1 | transitions2
    for f in final1:
        transitions.add((f, "lambda", start2))

    return (states1 | states2, alphabet1 | alphabet2, transitions, start1, final2)

# cazul 6: e = e1*
def star(e1):
    states1, alphabet1, transitions1, start1, final1 = e1

    start = new_state()
    final = new_state()
    states = states1 | {start, final}

    transitions = transitions1 | {(start, "lambda", start1), (start, "lambda", final)}
    for f in final1:
        transitions.add((f, "lambda", start1))
        transitions.add((f, "lambda", final))

    return (states, alphabet1, transitions, start, {final})

# cazul 7: e = e1+
def plus(e1):
    return concatenation(e1, star(e1))

# cazul 8: e = e1?
def optional(e1):
    alphabet1 = e1[1]
    return union(e1, cuvantul_vid(alphabet1))