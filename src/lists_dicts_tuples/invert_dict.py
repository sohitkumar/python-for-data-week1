d = {"a":1,"b":1,"c":2}
d1 = {}
for x in d:
    value = d[x]
    d1[value] = d1.get(value ,[])
    d1[value].append(x)
print(d1)