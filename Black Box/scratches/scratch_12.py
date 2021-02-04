# with open('/home/xela/py/some20.txt', 'r') as f:
#     strings = [s.rstrip() for s in f.readlines()]
# ff = open('/home/xela/py/11.txt','w')
# otsenki = [s.split(';')[1:] for s in strings]
# for x in otsenki:
#     print(sum(map(int, x))/len(x),file=ff)
# sr_mat = sum([int(x[0]) for x in otsenki]) / len(otsenki)
# sr_fiz = sum([int(x[1]) for x in otsenki]) / len(otsenki)
# sr_rus = sum([int(x[2]) for x in otsenki]) / len(otsenki)
# print(sr_mat, sr_fiz, sr_rus,file=ff)

import re
with open ('/home/xela/py/some32.txt', 'r') as a: a=str(a.read().split())
ff = open('/home/xela/py/1234.txt','w'); g1,g2,g3=[],[],[]
n = re.sub('[^0-9]', ' ', a);n=n.split();n=map(int, n);n=list(n)
print(n)
tot=[n[i:i+3] for i in range(0,len(n),3)]
for i in tot: g1.append(i[0]); g2.append(i[1]); g3.append(i[2])
# for ss in tot: print(sum(ss) / 3)
# print(sum(g1)/len(g1), sum(g2)/len(g2), sum(g3)/len(g3),file=ff)
# print(tot)