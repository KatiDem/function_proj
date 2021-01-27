def summ(*args):
    summary = 0
    n = 0
    for i in args:
        summary += i * args[n]
        n += 1
    print(summary)


summ(1, 2, 3, 4)
