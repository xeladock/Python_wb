a = int(input())
if (a in range(1,1000,10))  and (a not in range(11,1000,100)):
    print(a, 'программист')
elif a not in range(11,1000,100) and (a not in range(12,1000,100)) and a not in range(13,1000,100) and a not in range(14,1000,100) and ((a in range(2,1000,10))or ((a in range(3,1000,10))) or ((a in range(4,1000,10)))):
    print(a,'программиста')
else:
    print(a,'программистов')
