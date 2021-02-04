import re
with open ('some32.txt','r') as a: a=str(a.read().split())
ff = open('1234.txt','w'); g1,g2,g3=[],[],[]
n = re.sub('[^0-9]', ' ', a);n=n.split();n=map(int, n);n=list(n)
tot=[n[i:i+3] for i in range(0,len(n),3)]
for i in tot: g1.append(i[0]); g2.append(i[1]); g3.append(i[2])
for ss in tot: print(sum(ss) / 3,file=ff)
print(sum(g1)/len(g1), sum(g2)/len(g2), sum(g3)/len(g3),file=ff)
