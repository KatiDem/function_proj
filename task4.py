def sorting(*args):
    summ = 0
    n = 0
    maxim = 0
    for i in args:
        summ += i
        if i > args[n - 1] and i > maxim:
            maxim = i
        n += 1
    return summ, maxim


summ, maxim = sorting(1, 45, 6, 2, 5, 3)
print(maxim)
