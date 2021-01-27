def factorial(n):
    n = int(input('n = '))
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print(f'Factorial is {fact}')
    return fact

factorial(1)
