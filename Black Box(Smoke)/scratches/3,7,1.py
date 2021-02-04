from collections import Counter
a=int(input())
# c=[]
e=[]
m=[]
nn=[]
k=[]
# fq=[]
# iq=3[]
# hq=[]
n=0
while n!=a:
    b=input(str()).split(';')
    if int(b[1]) < int(b[3]):
        e.append(b[2])
        e.append('3')
        e.append(b[0])
        e.append('0')
    if int(b[1]) > int(b[3]):
        e.append(b[0])
        e.append('3')
        e.append(b[2])
        e.append('0')
    if int(b[1])==int(b[3]):
        e.append(b[0])
        e.append('1')
        e.append(b[2])
        e.append('1')
    # c=c+b
    n+=1
# for g in range(0,len(e)):
#     print(g)
# tot = [e[i] for i in range(0, len(e), 1)]
# print(tot)
# print(Counter(tot))
# print(e)

# e = [e[i:i + 1] for i in range(0, len(e), 2)]
e+=[['0','0'],['0','0']]
e.insert(0,'000')
# print(e)
# # print(Counter(e))
for g in range(0,len(e), 1):
    if e[g]=='000': continue
    if e[g] == ['0', '0']:
        break
    if e[g+1] == '3':
        m.append(e[g])
        m.append('1')
        # print(e[g],  'win')
    if e[g+1] == '1':
        nn.append(e[g])
        nn.append('1')
    if e[g+1] == '0':
        k.append(e[g])
        k.append('1')

        # print(e[g], 'lose')
    # else:
    #     break
m = [m[i:i+2] for i in range(0, len(m),2 )]
nn = [nn[i:i+2] for i in range(0, len(nn),2 )]
k = [k[i:i+2] for i in range(0, len(k),2 )]
# print(m)
print(nn)
# print(k)
for x in set(map(tuple, m)):
    print (x[0], m.count(list(x)),end=',')
print()
for x in set(map(tuple, k)):
    print (x[0], m.count(list(x)),end=',')
print()
for nn in set(map(tuple, nn)):
    if len(nn)==0:
        print('empty')

    else:
        print (x[0], m.count(list(nn)),end=',')
print()
# nn = [m[i:i+2] for i in range(0, len(m),2 )]





# m=map(tuple,m)
# m=Counter(map(tuple,m))
# m=Counter(m)
# for mm in set(m):
# # for mm in set(m):
#     print (mm, "=", m(tuple(mm)))
# print(nn)
# print(k)


    # else:
    #         print(e[g], end=' ')
    # elif '3' in e[g]:
    #     # print(Counter(e))
    #     print((e[g]), e.count(e[g]), 'побед')
    #     fq.append(g)
    # elif '1' in e[g]:
    #     print((e[g]), e.count(e[g]), 'ничья')
    #     iq.append(g)
    # elif '0' in e[g]:
    #     print((e[g]), e.count(e[g]),'поражений')
    #     hq.append(g)
    # else: continue
# print(fq)
# print(i)
# print(h)
# print(у)
    # elif e[g]==e[g+2]:
    #     print((e[g]))
    # elif e[g]==['0','0']:
    #     exit()
# for z,x in enumerate(e):
#     print(sorted(x))
    # for m in x:
    #     x=str(x)
    #     print(m.count(x))

    # print(z,x)

# c+=['-1','-1']
# c.insert(0,'-1')
# print(c)
# for hh,ss in enumerate(c):
#     if ss[hh]>ss[hh+2]:
#         e.append(ss)
#     if ss[hh] < ss[hh + 2]:
#         f.append(ss)
#     if ss[hh] == ss[hh + 2]:
#         h.append(ss)
#     else:
#         gg.append(ss)

    # print(hh,ss)
    # for g in range(0,len(h),2):
    #     if g=='-1': continue
    #     elif h[g]>h[g+2]:
    #         e.append(h[g])
    #     elif int(h[g])<int(h[g+2]):
    #             f.append(h[g])
    #     elif int(h[g])==int(h[g+2]):
    #             h.append(h[g])
    #     else:
    #         gg.append(h[g])
    # print(h,g)
# for g in range(0,len(c)+1,2):
#     if c[g]=='-1':
#         continue
#     elif int(c[g])>int(c[g+2]):
#         e.append(c[g])
#     elif int(c[g])<int(c[g+2]):
#         f.append(c[g])
#     elif int(c[g])==int(c[g+2]):
#         h.append(c[g])
#     else:
#     # if c[g]
#         gg.append(c[g])

# print(f)
# print(i)
# print(gg)
# print(int(c[0])+int(c[3]))
# d = dict(c.split(',') for i in c.split(','))
# print(d)
# result = [{}]
# for item in c:
#     key, val = item.split(",", 1)
#     if key in result[-1]:
#         result.append({})
#     result[-1][key] = val
# print(result)
    # tot = [n[i:i + 3] for i in range(0, len(n), 3)]
# for z,x in enumerate(c):
#     print(z,x)
# tot = [c[i:i + 2] for i in range(0, len(c), 2)]
#
# for k, v in tot.items():
#     print(k, v)
# b = dict(tot[:1])
# print(b)
# print(tot[0])
# tot = [e[i:i + 2] for i in range(0, len(e), 2)]
# print(tot)
# for z,x in enumerate(tot):
#     x=dict(x)
#     print(z,x)
# for g in range(0,len(c)-1):
#     if c[g[1]]> c[g+1[1]]:
#         e.append(g)
#     elif c[g] == c[g+1]:
#         f.append(g)
#         gg.append(g)
#     else:
#         h.append(g)

    # if tot[g]
# for i in tot:
#     for s in i:
#
#             if s
#             print(s)
# print(tot)
# print(e)
# print(f)
# print(gg)
# print(h)
# print(type(i))
# for x in range(0,len(tot)-1):
#
#     print(x)