a,b,c = float(input()),float(input()),str(input())
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    if b==0:
        print('Деление на 0!')
    else:
        print(a/b)
elif c=='mod':
    if b==0:
        print('Деление на 0!')
    else:
        print(a%b)
elif c=='pow':
    print(a**b)
elif c=='div':
    if b==0:
        print('Деление на 0!')
    else:
        print(a//b)
else:
    print('Неизвестная операция')
