import math
c = str(input())
if c=='треугольник':
    b, a, d = float(input()),float(input()),float(input())
    p = (b + a + d) / 2; print(math.sqrt(p * ((p - a) * (p - b) * (p - d))))
elif c=='прямоугольник':
    b, a = float(input()),float(input()); print(b*a)
elif c=='круг':
    b=float(input()); r=3.14; print(r*(b**2))
else:
    print('Неизвестный объект')
