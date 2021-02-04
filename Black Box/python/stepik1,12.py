# import math
# a,b,c = int(input()),int(input()),int(input())
# p=(a+b+c)/2print(math.sqrt(p*((p-a)*(p-b)*(p-c))))

# a = int(input()); print((-15<a<=12) or (14<a<17) or (19<=a))

# a,b,c = float(input()),float(input()),str(input())
# if c == '+':
#     print(a+b)
# elif c == '-':
#     print(a-b)
# elif c=='*':
#     print(a*b)
# elif c=='/':
#     if b==0:
#         print('Деление на 0!')
#     else:
#         print(a/b)
# elif c=='mod':
#     if b==0:
#         print('Деление на 0!')
#     else:
#         print(a%b)
# elif c=='pow':
#     print(a**b)
# elif c=='div':
#     if b==0:
#         print('Деление на 0!')
#     else:
#         print(a//b)
# else:
#     print('Неизвестная операция')


# import math
# c = str(input())
# if c=='треугольник':
#     b, a, d = float(input()),float(input()),float(input())
#     p = (b + a + d) / 2; print(math.sqrt(p * ((p - a) * (p - b) * (p - d))))
# elif c=='прямоугольник':
#     b, a = float(input()),float(input()); print(b*a)
# elif c=='круг':
#     b=float(input()); r=3.14; print(r*(b**2))
# else:
#     print('Неизвестный объект')

# a,b,c = int(input()),int(input()),int(input())
# if ((a>=c and a>=b) and (b<=a and b<=c)):
#     print(a,b,c,sep = '\n')
# elif ((a>=c and a>=b) and (c<=a and c<=b)):
#     print(a,c,b,sep = '\n')
# elif ((b>=c and b>=a) and (a<=b and a>=c)):
#     print(b,c,a,sep = '\n')
# elif ((b>=c and b>=a) and (c<=b and c>=a)):
#     print(b,a,c,sep = '\n')
# elif ((c>=a and c>=b) and (b>=a and b<=c)):
#     print(c,a,b,sep = '\n')
# elif ((c>=a and c>=b) and (a>=b and a<=c)):
#     print(c,b,a,sep = '\n')

# x,y,z = int(input()),int(input()),int(input())
# a = min(x,y,z); b = max(x,y,z); c!=a or c!=b
# print(b,a,c,sep = '\n')


# c = input()
# print(sum(int(c[0]),int(c[1]),int(c[2])))
# print(sum(int(c[3]),int(c[4]),int(c[5])))
# print(r,l)

# import math; a = input()
# print ('Счастливый' if  math.fsum((int(a[0]),int(a[1]),int(a[2])))==math.fsum((int(a[3]),int(a[4]),int(a[5]))) else 'Обычный')
#     print('Счастливый')
# else:
#     print('Обычный')

a = int(input())
if (a in range(1,1000,10))  and (a not in range(11,1000,100)):
    print(a, 'программист')
elif a not in range(11,1000,100) and (a not in range(12,1000,100)) and a not in range(13,1000,100) and a not in range(14,1000,100) and ((a in range(2,1000,10))or ((a in range(3,1000,10))) or ((a in range(4,1000,10)))):
    print(a,'программиста')
else:
    print(a,'программистов')

# '''(a not in range(1,1000,100) '''
# and a!=111
# or (a in range(1,1000,100))


