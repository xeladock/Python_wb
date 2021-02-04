with open ('some.txt', 'r') as a: a=a.read().lower().split(); b={}
for m in set(a): b.setdefault(m,[]).append(a.count(m))
print(max(b,key=b.get), *max(list(b.values())))
