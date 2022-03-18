# first task
def is_continues_sequence(it):
    k = 0
    for i in range(len(it) - 1):
        if it[i] + 1 == it[i + 1]:
            k += 1
    if k == len(it) - 1:
        return True
    else:
        return False


f = [-3, -2, -1, 0, 1, 2, 3]
s = [1, 2, 3, 5, 6, 7, 8, 9, 10]

print(is_continues_sequence(f))
print(is_continues_sequence(s))


# second task
def find_longest_length(stroke):
    maxcnt = 0
    premax = 0
    for i in range(len(stroke)):
        while stroke[i] != stroke[i + 1]:
            premax += 1
            if i < len(stroke):
                i += 1
            elif premax > maxcnt:
                maxcnt = premax
                return maxcnt
            if i + 1 <= len(stroke):
                pass
            else:
                break
        if premax > maxcnt:
            maxcnt = premax
    return maxcnt


print(find_longest_length('abcdeef'))
print(find_longest_length('jabjcdel'))

