
ab = []

a = int(input('enter marks in maths: '))
b = int(input('enter marks in english: '))
c = int(input('enter marks in science: '))

ab.append(a)
ab.append(b)
ab.append(c)

d = ab[0] + ab[1] + ab[2]
e = d / 3

if e >= 33:
    print('passes')

else:
    print('fails')