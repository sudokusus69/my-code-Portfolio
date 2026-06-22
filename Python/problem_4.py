a = input('enter your name: ')

if len(a) >= 10:
    print('name is too long')
elif len(a) <= 3:
    print('name is too short')
else:
    print('pass')