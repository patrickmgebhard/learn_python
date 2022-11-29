fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]

"""mini_batches = [training_data[k:k+mini_batch_size] for k in xrange(0, n, mini_batch_size)]"""     
training_data = [(1, 2), (3, 4), (5, 6)]

for x in fruits:
    print(x)

for x in "banana":
    print(x)

for x in range(6):
    print(x)

for x in adj:
    for y in fruits:
        print(x, y)

print(zip(adj, fruits))

for x, y in zip(adj, fruits):
    print(x, y)

for x in training_data:
    print(x)

for x, y in training_data:
    print(y)

for x, y in training_data:
    print(x, y)