a,b,c,e=input(str()),input(str()),input(str()),input(str()); d=dict(zip(a,b))
for c1 in c:
    for key,value in d.items():
        if c1 == key: print(value,end='')
print()
for e1 in e:
    for key,value in d.items():
        if e1 == value: print(key,end='')
