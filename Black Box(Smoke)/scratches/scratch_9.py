##3.4.2
with open ('/home/xela/py/some6.txt', 'r') as a: a=a.read().lower().split(); b={}
for m in set(a): b.setdefault(m,[]).append(a.count(m))
print(max(b,key=b.get), *max(list(b.values())))
словари + двумерный цикл = вот такая красота