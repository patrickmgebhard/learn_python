fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]

for x in fruits:
    print(x)

for x in "banana":
    print(x)

for x in range(6):
    print(x)

for x in adj:
    for y in fruits:
        print(x, y)

for x, y in zip(adj, fruits):
    print(x, y)