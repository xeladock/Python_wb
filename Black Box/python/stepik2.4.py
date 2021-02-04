# a, ag, ac=str.lower(input()),0,0
# for i in a:
#     if i == 'c': ac=ac+1
#     if i == 'g': ag=ag+1
# print(((ag+ac)/len(a))*100)
# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])фс
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])
# print(s)

# ac=str.lower(input())
# print(ac, len(ac),sep='')

# ac=str.lower(input())
# n=0
# for i in ac:
#     # i=str()
#     if i[::1]==i[::1+1]:
#         m=i
#         n=n+1
# print(n)
# # print(ac.count('a'))
# ac=str.lower(input())
# print(ac[1:])
# print(ac[::1])

# ac=str.lower(input())
# ss=len(ac)
# # a = ac.split()
# # m=ac[1:]
# # print(m)
# n=0
# if ss==1:
#     print(ac,'1',sep='')
# else:
#     for i in ac:
#         print(i)
    #     # if
    #     if i==(ss-1):
    #
    #     if ac[i]==ac[i+1]:
    #         n=n+1
    # print(n)

#     n=n+1
# print(n)
# n=0
# for i in ac:
#
#     # if i[0:1]==i[1:1]:
#     #     n=n+1
#     print(n)

#     # m=i[::]
#     print(i[1:])
        # n=n+1
    # print(s, end=' ')
    # print(s)
# print(ac)
    # print(n, end=' :

# a=str(input())
# b=[]
# g=[]
# # j=[]
# c=1
# e=1
# d=''
# if len(a)==1:
#     print(a)
# for s in a:
#     b.append(s)
# b+=['0']
# m = len(b)-1
# # print(m)
#
#     # print(s, end=' ')
# for x in range(0,m):
#     n = str(b[x])
#     if b[x] == b[x + 1]:
#         c=c+1
#         d=n+str(c)
#         # g.append(max(d))
#         # f=max(g)
#         # j.append(f)
#     elif b[x] != b[x + 1]:
#         g.append(d)
#         # d = d + str(a[x])
#         c=1
#         d=b[x+1]+str(1)
#         # g.append(d)
#     # print(b[x],c,sep='',end='')
# for gg in g:
#     print(gg,sep='',end='')

    # aaaabbcaa


# print('len',m)
    # if b[y]==b[y+1]:
    #     print('oja')
    # if d[0]==d[1]:
    #     print('ok')

# print(b)aa
# print(b[1]+b[0])
# print(s[2])
#     print(s[1], end=' ')


a=str(input())
b,g,c,d=[],[],1,''
if len(a)==1:
    print(a+str(1)); exit()
for s in a: b.append(s)
b+=['0']
for x in range(0,len(b)-1):
    n = str(b[x])
    if b[x] == b[x + 1]:
        c=c+1; d=str(b[x])+str(c)
    elif b[x] != b[x + 1]:
        if d=='': d=str(b[x])+str(1)
        g.append(d)
        c=1
        d=n+str(1)
for gg in g:
    print(gg,sep='')