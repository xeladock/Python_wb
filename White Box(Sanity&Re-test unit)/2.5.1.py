a,b=[int(x) for x in input().split()],[]
if len(a)==1: print(*a); exit()
a.append(a[0])
for g in range(0,len(a)-1):
    m=a[g-1]+a[g+1]; b.append(m)
b.remove(b[0])
c=(a[1]+a[-2])
b.insert(0,c); print(*b)
