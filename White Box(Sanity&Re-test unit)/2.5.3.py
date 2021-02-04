a=input().split()
for i in list(set(a)):
    if a.count(i) == 1: a.remove(i)
for g in list(set(a)):
    print(g, end=' ')
