

def discriminant(a, b, c):
    '''Функция вычисления дискриминанта'''
    return b**2 - 4 * a * c


def solve(a, b, c):
    '''Функция, которая вычисляет корни квадратного уравнения'''
    d = discriminant(a, b, c)
    if d < 0:
        print('Корней нет')
    elif d == 0:
        x = -b/(2*a)
        print(f'Один корень, x = {x}')
    elif d > 0:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print(f'Два корня, x1 = {x1}, x2 = {x2}')


solve(1,2,1)

solve(2, 5, 3)

solve(1, -1, 3)

solve(1, 0, 5)

solve(2, 10, 5)


def Test():
    pass
