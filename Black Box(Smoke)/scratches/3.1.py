# def f(n):
#     return n * 10 + 5
# print(f(f(f(10))))

# def min2(a,b):
#     if a<=b:
#         return a
#     else:
#         return b
# print(min2(min2(10,20),5))

# def foo():
#     return
# print(foo())

# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# print((*more_numbers))

# (A)

# s1='Привет! Я "короткая" строка.\nТут я начинаюсь с новой строки,\tа тут с новой строки и отступа'
# print(s1)

# def mp():
#     print(1)
# x=2
# print(mp(),x)

# def qq(m):
#     m.append(0)
#     m=[100]
# a=[]
# qq(a)
# print(a)
# x=input()


# def f(x):
#     if x<=-2:
#         print(1-((x+2)**2))
#         return ''
#     elif -2<x<=2:
#         print(-x/2)
#         return ''
#     elif 2<x:
#         print(1+((x-2)**2))
#         return''
# print(f(float(input())))

# def modify_list(l):
#     # l=[int(a) for a in input().split()]
#     # for a in lst:
#         if l[a]%2!=0:
#
#         else: print(a//2)
#         return''
# print (modify_list(int(input())))

# def min(a,b):
#     if a<=b:
#         return a
#     else:
#         return b
# m=min(min(42,15),min(47,78))
# print(m)

# def min(*a):
#     m=a[0]
#     for x in a:
#         if m>x:
#             m=x
#     return m
# m=min(min(42,17),min(47,78))
# print(m)
# a=int(input())
# b=int(input())
# s=int(input())
# def mr(a,b,s):
#     res=[]
#     if s>0:
#         x=a
#         while x<b:
#             res+=[x]
#             x+=s
#     elif s<0:
#         x=a
#         while x>b:
#             res +=[x]
#             x+=s
#     return res
# print(*mr(2,10,1))


# def pr():
#     print(a)
# a=2
# pr()
# lst = [1, 2, 3, 4, 5, 6]
def modify_list(l):
    # lst=[]
    b=[]
    for a in l:
        if a%2!=0: continue
        else: a = a // 2; b.append(int(a))
    l.clear()
    l.extend(b)
    # for g in b: l.append(g)
    return
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]
lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

