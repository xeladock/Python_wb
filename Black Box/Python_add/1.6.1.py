a=str(input()).split()
b=''
for m in a:
    b+=m
    b+=str('_')
print(b[:-1])
# a=a.lstrip(a)
# a=a.replace(' ','_')
# print(a)