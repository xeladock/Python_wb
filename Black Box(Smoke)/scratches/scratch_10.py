##3.4.3
# try:
#     k = 1 / 0
# except ZeroDivisionError:
#     k = 0
# print(k)
import re
# from string import digits
# from string import ascii_letters
##3.4.3
with open ('/home/xela/py/some32.txt', 'r') as a: a=a.read().lower().split()
ff = open('/home/xela/py/123.txt','w')
g1,g2,g3=[],[],[]# print(a)
m=str(a)

# n = ''.join(m for m in a if m.isdigit())
# n = filter(str.isdigit, m)
# n = "".join(n)
# n=m.translate(None,ascii_letters).strip("_")
n = re.sub('[^0-9]', ' ', m)
n=n.split()
n=map(int, n)
n=list(n)
tot=[n[i:i+3] for i in range(0,len(n),3)]
print(tot)
for item in tot:
        g1.append(item[0])
        g2.append(item[1])
        g3.append(item[2])
for ss in tot:
    print(sum(ss) / 3,file=ff)
    # print(round(sum(ss) / 3, 4), file=ff)

# print(nnn)
# print(tot)
print(sum(g1)/len(g1), sum(g2)/len(g2), sum(g3)/len(g3),file=ff)
# print(round(sum(g1)/3,9), round(sum(g2)/3,9), round(sum(g3)/3,9),file=ff )
# with open ('/home/xela/py/1', 'w') as aaa:
    # aaa.write(print(sum(g1)/3, sum(g2)/3, sum(g3)/3 ))
    # aaa.write(str(25))

# print(sum(tot[0])/3)
# print(lll)

# n=n.replace('          ','')
# p=[n]

# aa=p.split(); bb=map(int, aa);aa=list(bb)
# print(n)
# print(aa)

# gg=[str(i) for i in range(0,100)]
# # b={}
# aa=ord('a'); c=[chr(i) for i in range(aa,aa+26)]
# for x in range(0,len(a)-1):
#     if a[x] in in gg: continue
#     else: g.append(a[x])
# print(g)
# print(type(nnn))
# i=0
# for b in a:
#     print(b)
# print(type(b))

    # if b in c:
    #     d.append(b)
    #     print(d)
    # else: continue
# print(*d)
# e=list(d)
#     print(d)
# print(type(*d))
# a=a.split(); b=map(int, a);a=list(b)
# d= d.split()
# m = map(int, d)
# l = list(d)
# print(l)