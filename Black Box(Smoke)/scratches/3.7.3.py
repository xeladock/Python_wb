a=int(input());x=[];n=1
while n!=a+1: x+=[(str(input()).lower())]; n=n+1
    # m.append(x)
a=int(input());n=1;z=[]
while n!=a+1:
    z+=([str(input()).lower().split()]); n=n+1
    # f.append(x)
z=list(set([item for sublist in z for item in sublist]))
for zz in z:
    if zz not in x: print(zz)

# print(x)
# print(z)
# print(ff)