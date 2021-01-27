def my_func(a, b):
    a = int(input('a = '))
    b = int(input('b = '))
    summ = a + b
    print(f'{a} + {b} = {summ}')
    return summ


a = my_func(1, 1)
print(a)
