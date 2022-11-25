languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6, 8]
opinions = ['good', 'bad', 'medium']

# so the zip function takes iterables and returns a list of tuples based on the iterable objects
# the shortest iterable defines the length in this example 3
result = zip(languages, versions, opinions)
print((result))
print(result[0])
print(result[0][0])