import itertools
with open ('/home/xela/py/77.txt', 'r') as a: a=a.read().lower().split(); ff = open('/home/xela/py/777.txt','w')
w,zz=[],[]
a.insert(0,'text');a.insert(0,'text');del a[::3];a.pop(0)
tot = [a[i:i+2] for i in range(0, len(a), 2)]
n=[list(item[1]) for item in itertools.groupby(sorted(tot), key=lambda x: x[0])]
for s in n: w.append(list(itertools.chain.from_iterable(s)))
for ww in w:
    s=ww[0];zz.append(int(s))
    del ww[::2];ww.insert(0, s)
    ww = list(map(int, ww));ww=(sum(ww[1:])/ (len(ww) - 1));zz.append(ww)
zz = [zz[i:i+2] for i in range(0, len(zz),2)]
for zzz in sorted(zz):
    if len(zzz) == 1: print(*zzz, '-',file=ff)
    else: print(*zzz,file=ff)
# print(sorted(zz))fi
    # ww.pop(0)
    # print(s, ww,file=ff)