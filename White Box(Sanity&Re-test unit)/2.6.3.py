a = input(). split()
b = input()
e,f=0,[]
if b not in a:
    print('Отсутствует')
for i in a:
    e=e+1
    if i==b: f.append(e)
    if i!=b: f.append(0)
for z in f:
    if z==0: continue
    else: print(z-1,end=' ')
