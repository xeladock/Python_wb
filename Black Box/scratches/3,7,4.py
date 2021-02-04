# a=int(input());x=[];n=1;
x = [input().split() for x in range(int(input()))];c1,c2=[],[]
print(x)
# while n!=a+1: x += [(str(input()).lower()).split()]; n+=1
for xx in x:
        if 'восток' in xx: c1.append(int(xx[1]))
        if 'запад' in xx: c1.append(int(xx[1])*(-1))
        if 'север' in xx: c2.append(int(xx[1]))
        if 'юг' in xx: c2.append(int(xx[1])*(-1))
print(sum(c1),sum(c2))
# print(c1)
# print(c2)