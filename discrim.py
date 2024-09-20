a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

D = b**2 - 4 * a * c

if D > 0:
    x1 = (-b + D**0.5)/2*a
    x2 = (-b - D**0.5)/2*a
    print(x1)
    print(x2)
elif D == 0:
    x = -b/2*a
    print(x)
else:
    D < 0 
    print('Решения нет')
