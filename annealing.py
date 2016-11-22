import math
import random

funcs = {
    'random_state': None,
    'next_state': None,
    'energy': None,
    'temperature': None,
}

def optimize():
    for value in funcs.values():
        assert value is not None

    random_state = funcs['random_state']
    next_state = funcs['next_state']
    energy = funcs['energy']
    temperature = funcs['temperature']

    seq = random_state()

    for t in temperature():

        cur = next_state(seq)

        delta = energy(cur) - energy(seq)

        if delta <= 0:
            seq = cur
        else:
            p = math.exp(-delta / t)
            if random.random() < p:
                seq = cur

    return seq