##3.4.2
# with open ('/home/xela/py/some7.txt', 'r') as a: a=a.read().lower().split()
with open ('/home/xela/py/some7.txt', 'r') as a: a=a.read().lower().split()
b={}
for m in set(a): b.setdefault(m,[]).append(a.count(m))
# c=max(b,key=b.get); x=(list(b.values()))
print(max(b,key=b.get), *max(list(b.values())))