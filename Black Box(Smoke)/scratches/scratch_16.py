import itertools
a=int(input())
e=[]
w=[]
z=[]
c=0
while c!=a:
    # b=input(str())
    # if ':' in b:
    #     b=b.replace(':',';')
    # if ';;' in b:
    #     b=b.replace(';;',';')
    b = input().split(';')
    z.extend(b)
    if int(b[1]) < int(b[3]):
        e.append(b[2])
        e.append('03')
        e.append(b[0])
        e.append('0b')
        if int(b[1]) != int(b[3]):
            e.append(b[2])
            e.append('0pr')
            e.append(b[0])
            e.append('3l')
            e.append(b[0])
            e.append('0n')
            e.append(b[2])
            e.append('0n')
    if int(b[1]) > int(b[3]):
        e.append(b[0])
        e.append('03')
        e.append(b[2])
        e.append('0b')
        if int(b[1]) != int(b[3]):
                e.append(b[0])
                e.append('0pr')
                e.append(b[2])
                e.append('3l')
                e.append(b[0])
                e.append('0n')
                e.append(b[2])
                e.append('0n')
    if int(b[1])==int(b[3]):
        e.append(b[0])
        e.append('0nn')
        e.append(b[0])
        e.append('0b')
        e.append(b[0])
        e.append('0pr')
        e.append(b[2])
        e.append('0nn')
        e.append(b[2])
        e.append('0b')
        e.append(b[2])
        e.append('0pr')
    c+=1
# print(e)
# for zz in z:
#
# print(z)
e = [e[i:i+2] for i in range(0, len(e), 2)]
e=[list(item[1]) for item in itertools.groupby(sorted(e), key=lambda x: x[0])]
print(e)
for s in e:
    w.append(list(itertools.chain.from_iterable(s)))
print(w)
# e.clear()
for ww in w:
    s = ww[0]
    ww.insert(1, str(z.count(s)))
    ww.insert(0, s+str(':'))
    for www in ww:
        if s == www:
            ww.remove(www)
    for www in ww:
        if '03' not in ww:
            break
        else:
            ww.insert(2, int(ww.count('03')))
            ww.remove('03')
            break
    for www in ww:
        if '0nn' not in ww:
            break
        else:
            ww.insert(3, int(ww.count('0nn')))
            ww.remove('0nn')
            break
    for www in ww:
        if '3l' not in ww:
            break
        else:
            ww.insert(4, int(ww.count('3l')))
            ww.remove('3l')
            break
    for www in ww:
        if ww[2] == 1 or ww[2] == 2 or ww[2] == 3 or ww[2] == 4:
            break
        else:
            ww.insert(2, int(0))
            ww.remove(ww[3])
            break
    for www in ww:
        if ww[3] == 1 or ww[3] == 2 or ww[3] == 3 or ww[3] == 4:
            break
        else:
            ww.insert(3, int(0))
            ww.remove(ww[4])
            break
    for www in ww:
        if ww[4] == 1 or ww[4] == 2 or ww[4] == 3 or ww[4] == 4:
            break
        else:
            ww.insert(4, int(0))
            ww.remove(ww[5])
            break
    for www in ww:
        ww.insert(5,int(ww[2]*3+ww[3]))
        break
    print(ww[0]+ww[1], *ww[2:6])