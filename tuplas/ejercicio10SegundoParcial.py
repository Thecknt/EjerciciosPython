a = "SEGUNDO PARCIAL"
b = {}
for i in a.split():
    if i in b.keys():
        b[i] +=1
    else:
        b[i] = 1
k = tuple(b.keys())
for i in k:
    if b[i] > 1:
        del( b[i])

print(b)