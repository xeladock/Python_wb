c=[];d=0
a0,b0,an,bn=0,0,0,0
while 0==0:
    b = input().split()
    d+=1
    if 'end' in b:
        break
    g = len(b); c.append(b)
d-=1
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
        mat[i][j] = int(c[a0][j]) + int(c[an][j]) + int(c[i][b0]) + int(c[i][bn])
for mm in mat:
    print(*mm)
