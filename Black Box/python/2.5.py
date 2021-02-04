# students = ['Ivan', 'Masha', 'Sasha']
# ind=students.index('Sasha')
# print(ind)

# a = [1, 2, 3]
# b = a
# a[1] = 10
# b[0] = 20
# a = [5, 6]
# print(b)

# print(sum([int(i) for i in input().split()]))

# a=input().split()
# if len(a)==1:
#     print(a[0])
# else:
from collections import OrderedDict
# a=input().split()
# a=set(a)
# for i in a:
#     if a(i)>1:
#         print(i)
#
# a=[int(x) for x in input().split()]
# if a.count(x) >= 2:


# a=input().split()
# for i in list(set(a)):
#     if a.count(i) == 1:
#         a.remove(i)
# s=list(set(a))
# for g in s:
#     print(g, end=' ')

# a=input().split()
# s=list(set(a))
# print(s.sort())


# for g in s:
#     if s.count(g) > 1:
#         print(g, end=' ')
        # print(i, end=' ')
# m=list(i)
# for s in m:
#     if m.count(i) ==2:
#         print(m)
# print(m)
# m=map(int(i))
#
# # m=list(i)
# print(m)

# for m in i:
#     print(m)
# i=set(i)
# print(i)

# a,b=[int(x) for x in input().split()],[]
# if len(a)==1: print(*a); exit()
# a.append(a[0])
# for g in range(0,len(a)-1):
#     m=a[g-1]+a[g+1]; b.append(m)
# b.remove(b[0])
# c=a[1]+a[-2]
# b.insert(0,c); print(*b)
# # print()
# print(a[g])


a=input().split()
for i in list(set(a)):
    if a.count(i) == 1: a.remove(i)
# s=list(set(a))
for g in list(set(a)):
    # sorted(g)
    print(*sorted(g), end=' ')
#
# a = input().split()
# for i in list(set(a)):
#     if len(a) == 1: a.remove(i)
# for g in list(set(a)):
#     print(g, end=' ')

# a=input().split()
# b=[]
# for i in list(set(a)):
#     b.append(a.count(i))
# sorted(b)
# print(b)
# print(b.sort())