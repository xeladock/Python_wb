a=str(input())
b,g,c,d=[],[],1,''
if len(a)==1:
    print(a+str(1)); exit()
for s in a: b.append(s)
b+=['0']
for x in range(0,len(b)-1):
    n = str(b[x])
    if b[x] == b[x + 1]:
        c=c+1; d=n+str(c)
    elif b[x] != b[x + 1]:
        if d=='': d=n+str(1)
        g.append(d)
        c=1
        d=b[x+1]+str(1)
for gg in g:
    print(gg,sep='',end='')
