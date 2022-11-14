import random

def pick(big_stream):

    random_element = None
    for x, y in enumerate(big_stream):

        if x == 0:
            random_element = y

        elif random.randint(1, x + 1) == 1:
            random_element = y

    return random_element