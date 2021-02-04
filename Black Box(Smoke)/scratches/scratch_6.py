##3.4.1

with open ('/home/xela/py/some.txt', 'r') as a: a=a.readline()
aa=ord('a'); c=[chr(i) for i in range(aa,aa+26)]
bb=ord('A'); d=[chr(i) for i in range(bb,bb+26)]
e,g=[str(i) for i in range(0,10)],[]
# print(e)
# g=[]
# e,g=['0','1','2','3','4','5','6','7','8','9'],[]
for s in a:
    if s in c or s in d: g.append(s)
    if s not in e: a=a.replace(s,' ')
a=a.split(); b=map(int, a);a=list(b)
h=[x*z for x,z in zip(a,g)];
# print(*h==[x*z for x,z in zip(a,g)],sep='')
print(a)
print(c)
print(type(a))
# for m in enumerate(a):

# for m in range(0,len(a)-1):
#     if a[m] and a[m + 1] != ' ':
#
# for m in range(0,len(a)-1):
#     if a[m] == ' ': continue
#     elif a[m] and (a[m] and a[m+1])!= ' ':
#         h.append(a[m])

        #
# a=(a[1:])

# {h.split(",")}
# h.split(',')a3b4c2e10b1

# h.remove[0]
# for ab in a:
#     if ab==' ': continue
#     else:
#         f.append(ab)
    # elif s in e:
    #     f.append(s)
    # else:
    #     for s in e:
    #         if (e[s] and e[s+1]) not in c:
    #                     h=str (e[s] + e[s+1])
    #                     f.append(h)
    #                     h = ''
            # if e[s]==e[s+1]:



# print(a)
# for s in a:
#     b.append(s)
# for m in b:
#     if b[m]=
#     if m in c:
#         print(m)