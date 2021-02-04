a=[]
n=int(input())
m=int(input())

for i in range(n):
    b=[]
    for i in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)