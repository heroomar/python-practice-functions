def flat(l):
    out=[]
    for i in l:
        if isinstance(i,list):
            out.extend(flat(i))
        else:
            out.append(i)
    return out

l = [1, [2, [3, 4]], 5, [6, [7, [8]]]]
print("flat of list is:",flat(l))