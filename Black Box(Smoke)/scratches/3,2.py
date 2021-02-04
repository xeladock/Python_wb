# s=set()
# m ={1,2,3,4,5,5}
# print(6 in m)

# s=set()
# m ={0:1,1:2,2:3,3:4,4:5,5:5}
# m[6]='a'
# del m[2]
# print(m.get(6))
# print(m[0])
# print(m)

# m ={0:1,1:2,2:3,3:4,4:5,5:'a', 5:'b',6:6}
#
# for s in m.keys():
#     print(s, end=' ')
# print()
# for z in m.values():
#     print(z, end=' ')
# print()
# for x in m.items():
#     print(x,end=';')
# print()
# for s,z in m.items():
#     print(s,z,end='; ')

def update_dictionary(d, key, value):
    s=[]
    # m=[]
    # d={}
    if key in d:
        s.append(int(value/2))
        d[2]=s
    if key not in d:
        s.append(value)
        # m.append(s)
        d[2] = s
    elif 2 * key in d:
        # s.append(m)
        s.append(int((key * 2) / -2))
        d[2] = s
    elif 2 * key not in d:
        # s.append(m)
        s.append(int((key * 2)/-2))
        d[2] = s
    return
    # s.extend(s)
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)
# print(m)# {2: [-1, -2, -3]}
# a=str(input()).lower().split()
# for m in set(a): print(m, a.count(m))
    # if a[m] == a[m+1]:
    #     c=c+1
    #     print(a,c)
    # elif a[m] != a[m+1]:
# print(a.count(a))
# print(len(a))
# print(a)
# print(a[1])
# # for m in a:
#     if
#     # m.count(a)
#     print(m)
# print(a)

# a=int()
# print(f(a))
# a=int(input())
# b=[]
# for n in range (1,a+1):
#     b.append(n)
#
# print(b)
    # s=int(input())
    # while enumerate x,s
    # print(m)
# def f(x):
#     return (f(x-1) + f(x-2)) * 13 % 107
# a=int(input())
# n=1
# while n!=a+1:
#     z=0
#     z=int(input())
#     n=n+1
#     x=z
#     print(f(x))
#     exit()