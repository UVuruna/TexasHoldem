a = {1,7,3,4,5,6}
b = {4,2,3,1,5}

print(b.issubset(a))

Suits = [set() for _ in range(4)]
print(Suits)


c = [1,1,1,2,3,4,4]
for i in set(c):
    print(c.count(i))