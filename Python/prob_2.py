def name():
    a = input('input your name: ')

    if a.lower().startswith('s'):
        print('name starts with s')
    else:
        print('name does not start with s')

def factorial():
    n = int(input('input a number: '))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f'factorial of {n} is {fact}')

def star_pattern():
    n = int(input('input a number:'))
    for i in range(1,n+3,2):
        print('*' * i)


def star_bx_pattern():
    n = int(input('input a number: '))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


def reverse_table():
    n = int(input('input a number: '))
    for i in range(10, 0, -1):
        print(f'{n} * {i} = {n*i}')


