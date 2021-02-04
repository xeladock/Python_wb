def update_dictionary(d, key, value):
    s=[]
    if key in d:
        # m=key
        s.append(value)
        # d.update(key)
        d[key].append(s)
    if (key not in d):
        n=2*key
        s.append(n)
        d[2*key].append(value)
    if (2*key not in d):
        d[2*key].append(value)
d={}
print(update_dictionary(d,1,-1))
print(d)
# d={2:[-1]}
# a=2
# if a not in d:
#     d[2].append(a)
# print(d)
