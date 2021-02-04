a=int(input())
# c=[]
e=[]
l=[]
nn=[]
m=[]
lm=[]
lnn=[]
# fq=[]
# iq=3[]
# hq=[]
n=0
while n!=a:
    b=input(str()).split(';')
    if int(b[1]) < int(b[3]):
        e.append(b[2])
        e.append('3')
        e.append(b[0])
        e.append('0')
        if int(b[1]) != int(b[3]):
            l.append(b[0])
            l.append('3')
            l.append(b[2])
            l.append('0')
            nn.append(b[0])
            nn.append('0n')
            nn.append(b[2])
            nn.append('0n')
    if int(b[1]) > int(b[3]):
        e.append(b[0])
        e.append('3')
        e.append(b[2])
        e.append('0')
        if int(b[1]) != int(b[3]):
                l.append(b[0])
                l.append('0')
                l.append(b[2])
                l.append('3')
                nn.append(b[0])
                nn.append('0n')
                nn.append(b[2])
                nn.append('0n')
    if int(b[1])==int(b[3]):
        nn.append(b[0])
        nn.append('1n')
        nn.append(b[2])
        nn.append('1n')

    # c=c+b
    n+=1
# e = sorted([e[i:i + 2] for i in range(0, len(e), 2)])
# l = sorted([l[i:i + 2] for i in range(0, len(l), 2)])
# nn = sorted([nn[i:i + 2] for i in range(0, len(nn), 2)])
print(e)
print(l)
print(nn)
e+=[['0','0'],['0','0']]
e.insert(0,'000')
for g in range(0,len(e), 1):
    if e[g]=='000': continue
    if e[g] == ['0', '0']:
        break
    if e[g+1] == '3':
        m.append(e[g])
        m.append('1')

l+=[['0','0'],['0','0']]
l.insert(0,'000')
for g in range(0,len(l), 1):
    if l[g]=='000': continue
    if l[g] == ['0', '0']:
        break
    if l[g+1] == '3':
        lm.append(l[g])
        lm.append('1l')

nn+=[['0','0'],['0','0']]
nn.insert(0,'000')
for g in range(0,len(nn), 1):
    if nn[g]=='000': continue
    if nn[g] == ['0', '0']:
        break
    if nn[g+1] == '1n':
        lnn.append(nn[g])
        lnn.append('1')

# print(e)
# print(l)
# print(nn)
print(m)
print(lm)
print(lnn)