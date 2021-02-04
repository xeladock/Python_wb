# a = str(input())
# # a=[a]
# a=a.split()
# b=map(int, a)
# a=list(b)
# print(a)
with open ('/home/xela/py/some7.txt', 'r') as a: a=a.read().lower().split()
# a=str.lower().split()
# with open ('/home/xela/py/some6.txt', 'r') as
# a=open('/home/xela/py/some6.txt', 'r')
# a=a.read()
f=str
b={}
for m in set(a):
    # a.sort()
    b.setdefault(m,[]).append(a.count(m))
    # print(m, a.count(m))


c=max(b,key=b.get)
# c=max(b.items(),key=lambda x:x)
# for dd in b:
#     if d= c:
#         print(b.values())
# print(a)
# z=(list(b.keys()))
x=(list(b.values()))
# # f=str(d)
# for g in d:
#     print(g)
# print(f)
# print(list())
print(c, *max(x))
# print(c,d)
# print(z[x.index(max(x))])
# print()