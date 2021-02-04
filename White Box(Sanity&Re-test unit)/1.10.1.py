a, b, c=int(input()),int(input()),int(input())
if a<=c<=b:
    print('Это нормально')
elif c>=a and c>=b:
    print('Пересып')
elif c<=a and c<=b:
    print('Недосып')
