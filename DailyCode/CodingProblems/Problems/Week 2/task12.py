def staircase(n, X):

    cache = [0 for _ in range(n + 1)]
    cache[0] = 1

    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)
        cache[i] += 1 if i in X else 0
        
    return cache[-1]