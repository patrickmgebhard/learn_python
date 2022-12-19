import requests
from pprint import pprint

x = requests.get('https://w3schools.com/python/demopage.htm')

# pretty print all properties of an object
#pprint(vars(x))

# pretty print all functions and properties of a class
#pprint(dir(x))

for i in dir(x):
    print(i)