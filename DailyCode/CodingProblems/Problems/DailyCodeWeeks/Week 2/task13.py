def subStr(str, x):

    start, end = 0, x
    max_len = x

    while end <= len(str):

        if len(set(str[start: end])) <= x:
            current_len = end - start
            if current_len >= max_len:
                max_len = current_len
            end += 1

        else:
            start += 1

    return max_len

print(subStr("abcba", 1))
print(subStr("abcba", 2))
print(subStr("abcba", 3))