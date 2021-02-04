def modify_list(l):
    b=[]
    for a in l:
        if a%2!=0: continue
        else: a = a/2; b.append(int(a))
    l.clear(); l.extend(b)
lom = [10, 5, 8, 3]
modify_list(lom)
print(lom)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)