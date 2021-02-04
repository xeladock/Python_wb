def f(x):
    return (f(x-1) + f(x-2)) * 13 % 107
# d={}
a=int(input())
m=[]
n=1
while n!=a+1:
    x=int(input())
    n=n+1
    m.append(x)
for x in m:
    print(f(x))
# print(m)
    # exit()

# def f(x):
#     return (f(x-1) + f(x-2)) * 13 % 107
#
# x=2
# print(f(x))
# c=max(b.items(),key=lambda x : x[1])