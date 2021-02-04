a=(input().split())
b=(input())
if b not in a: print('None'); exit()
for m in range(len(a)):
   if a[m] == b:
    print(m.__index__(),end=' ')
#     print('ok')
# print(b)
    # if b==m[a]:
    #     print(m)