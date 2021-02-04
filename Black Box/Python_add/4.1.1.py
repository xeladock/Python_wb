import itertools
a=str(input());b=[];c=''

for m in a: b.append(m)
b=[list(item[1]) for item in itertools.groupby((b), key=lambda x: x[0])]
for bb in b:
    if len(bb) == 1:
        c+=bb[0]
    else:
        c+=(str(len(bb))+bb[0])
# c=c.replace('1','')
print(c)
# print(b)
# # b+['0']
# for m in range(len(a)):
#     # print(a[m])
#     if a[m]==a[m+1]:
#         b.append(m)
#     else:
#         b.append(' ')
# print(b)
