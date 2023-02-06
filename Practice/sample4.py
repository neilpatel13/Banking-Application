a = ["Bob", "Bill", "Pete", "John", "Smith", "Greg"]
c = {}

for i in a:
    num = 0
    for x in i:
        num += ord(x)
    c[i] = num
print(f"{c}")
