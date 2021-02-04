#своя задача
with open ('/home/xela/py/1/1.txt','r') as a:
    a=a.read().split()
with open ('/home/xela/py/1/2.txt','r') as b:
    b=b.read().split()
c = open('/home/xela/py/1/3.txt','w')
d=[]
# print((a))
# print((b))
for m in b:
    # for mm in b:
        if m not in a:
            print(m, file=c)