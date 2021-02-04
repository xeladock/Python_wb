def update_dictionary(d, key, value):
    s=[]
    if key in d:
        s.append(value)
        d[key].append(*s)
    elif 2*key in d:
        s.append(value)
        d[2*key].append(*s)
    else:
        s.append(value)
        d[2*key] = []
        d[2*key].append(*s)
