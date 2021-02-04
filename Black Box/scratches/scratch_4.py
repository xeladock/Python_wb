def update_dictionary(d, key, value):
    s=[]
    # m=[]
    # d={}
    if key in d:
        s.append(int(value/2))
        d[2]=s
    if key not in d:
        s.append(value)
        # m.append(s)
        d[2] = s
    elif 2 * key in d:
        # s.append(m)
        s.append(int((key * 2) / -2))
        d[2] = s
    elif 2 * key not in d:
        # s.append(m)
        s.append(int((key * 2)/-2))
        d[2] = s
    return
    # s.extend(s)
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)