# https://realpython.com/python-lambda/
#test

def add_one(x):
    return x + 1

add_one_lambda = lambda x: x + 1

print(add_one_lambda(2))

print((lambda x: x * x)(3))