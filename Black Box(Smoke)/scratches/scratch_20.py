# s=[i for i in range(10)]
# print(5 in s)
# print(s)

# def update_dictionary(d, key, value):
#     s=[]
#     if key in d:
#         s.append(value)
#         d[key].append(*s)
#     elif 2*key in d:
#         s.append(value)
#         d[key].append(*s)
#     else:
#         s.append(value)
#         # d[2*key] = s
#         d[2*key].append(*s)
# d={}
# print(update_dictionary(d,1,-1))
# print(d)
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)
# d={}
# # s=[]
# # s=[10]
# key=3
# value=5
# # print(s)
# d[key]=[]
# d[key]=value
#
# print(*d.values())

# d = {1: 20, 2: 40, 3: 90}
# print(d.keys[1])


# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     elif 2*key in d:
#         d[2*key].append(value)
#     else:
#         d[2*key] = []
#         d[2*key].append(value)
# d={}
# print(update_dictionary(d,1,-1))
# print(d)


# def update_dictionary(d, key, value):
#     key=key+1
#     value=value+2
# d = {}
# print(update_dictionary(d, 1, -1))
# print(d)
# key=2
# if key in d:
#     print('ok')
#     # print('ключ есть')
# elif key is not d:
#     print('not ok')
# d[2*key]=[]
# key=1
# s=5
# # d[key].append(s)
# d[d.keys()].append(s)
# print(d)

# d={10:1001,10:1000}
# print(d.values())
# a=[]
# for n,m in enumerate(d):
#     # a.append(m)
#     print(n,m)

# l=[]
# l(l.keys(d))
# print(l)
# s=[]
# ss=[]
# s(d.keys())
# print(s)
# for key in ss.keys(d):
#     print(key)

# s.append(d.keys())
# print(*s[0] .join (ss in ss))
# print(ss)
# s=''
# s=d.keys()
# s=d.join())
# print(s)
# print(d[10])

# def c(m):
#     try:
#         m=int(m)
#     except ValueError as i:
#
#         print(i)
#         m=0
#     except TypeError:
#         pass
#     except FileNotFoundError:
#         pass
#
#     # else:
#         # m=0
#     #1000:10=m:x
#     return 10 *m /1000
#     # finally:
#     #     print('totally stop')
# print(c('a'))

# a=input()
# try:
#     a=int(a)
#     print(a)
# except:
#     pass

# def f(x):
#     return (f(x-1) + f(x-2)) * 13 % 107
#
#
# d = {}
# a = []
#
# for _ in range(int(input())):
#     x = int(input())
#     while True:
#         try:
#             a.append(d[x])
#             break
#         except KeyError:
#             d[x] = f(x)
#
# print(*a)

# a=['1','2','3','4']
# b=['a','b','c','d']
# c=[x+z for x,z in zip(a,b)]
# # b=input(str())
# # # d=(zip(a,b))
# print(*c)

s=3
if (isinstance(s, str)):
    print('ok')
else:
    print('no')
