with open ('some.txt', 'r') as a: a=a.readline()
aa=ord('a'); c=[chr(i) for i in range(aa,aa+26)]
bb=ord('A'); d=[chr(i) for i in range(bb,bb+26)]
e,g=[str(i) for i in range(0,10)],[]
for s in a:
    if s in c or s in d: g.append(s)
    if s not in e: a=a.replace(s,' ')
a=a.split(); b=map(int, a);a=list(b)
h=[x*z for x,z in zip(a,g)]; print(*h,sep='')
