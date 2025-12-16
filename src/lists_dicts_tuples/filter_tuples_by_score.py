t = [("Ann",85),("Bob",72),("Cara",90)] 
threshold = 80
l = []
for i in t:
    if i[1] > threshold:
        l.append(i[0])
print(l)