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

