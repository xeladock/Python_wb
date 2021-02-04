
# c=[]
# e=[]
# d=0
# while 0==0:
#     b = input().split()
#     c.append(b)
#     d=d+1
#     # if b=str:
#     #     exit()
#     if 'end' in b:
#         c.remove(c[-1])
#         # print()
#         break
# for m in c:
#     print(*m)


c=[]
b=''
# e=[]
d=0
a0,b0,an,bn=0,0,0,0
# g=0
while b!='end':
    b = input().split()
    d+=1
    if b=='end':
        # c.remove(c['end'])
        break
    g = len(b)
    # g.count(b)
    c.append(b)
# print(c)
# if len(c)==1:
#     for m in c:
#         for mm in m:
#             print(int(mm)*4)
#             exit()
# print (len(c))

print (g)
print(c) ##[['1', '4', '7']]
d-=1
# print(g)
mat=[[0 for j in range(g)] for i in range(d)]

for i in range(d):
    for j in range(g):
        if i - 1 < 0:
            a0 = d-1
        else: a0 = i - 1
        if j - 1 < 0:
            b0 = g - 1
        else: b0 = j - 1
        if i + 1 > d - 1:
            an = 0
        else: an = i + 1
        if j + 1 > g - 1:
            bn = 0
        else: bn = j + 1
        # print(c[a0][j])
        # print(c[an][j])
        # print(c[i][b0])
        # print(c[i][bn])
        mat[i][j] = int(c[a0][j]) + int(c[an][j]) + int(c[i][b0]) + int(c[i][bn])

for mm in mat:
    print(*mm)


        # print(i,j)

        # asum[i][j]=int([i]+[j])
        # mat=(str(c[i]+c[j]))
# for m in c:1
#     for mm in c:

# print(mat) #[[0]]
