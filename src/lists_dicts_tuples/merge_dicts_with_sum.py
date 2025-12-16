d1 = {"a":1,"b":2}
d2 = {"b":3,"c":4}

l = list(d1.keys()) + list(d2.keys())

d = {}
for i in l:
    d[i] = d1.get(i, 0) + d2.get(i, 0)
print(d)


# another approach

from collections import Counter
c = Counter(d1) + Counter(d2)
print(c)