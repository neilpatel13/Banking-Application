a = [1, 2, 3, 44, 5, 9, 6, 6, 8]
c ={}
for i in a:
    if i in c.keys():
        c[i] += 1
    else:
        c[i] = 1

print(f"{c}")