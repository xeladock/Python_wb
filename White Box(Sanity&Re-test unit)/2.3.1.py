a, b, c ,d =int(input()),int(input()),int(input()),int(input())
for j in range(c,d+1):
    print('\t',j, end='')
print()
for i in range(a,b+1):
    print(i,end='')
    for j in range(c, d + 1):
        s=j*i
        print('\t',s,end='')
    print()
