def staircase(x, y):

    cache = [0 for _ in range(x + 1)]
    cache[0] = 1

    for i in range(x + 1):
        cache[i] += sum(cache[i - x] for x in y if i - x > 0)
        cache[i] += 1 if i in y else 0

    return cache[-1]