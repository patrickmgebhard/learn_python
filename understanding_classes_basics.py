"""
-notes on https://docs.python.org/3/tutorial/classes.html
-what is self doing; self references the given instance of a class; you can use it to access the attributes and methods of the class in Python
"""
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
#print(x.__doc__)
#print(x.i)

# interesting learning that these two statements are equivalent, which shows that the instance object is given as the first argument to x.f(); Cool!
#print(x.f())
#print(MyClass.f(x))


# if you want to the new instance to have e.g. specific attributes you can do this in the __init__ function
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

y = Complex(3, 7)
#print(y.r, y.i)


# so there are class and instance specific variables
class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind, e.kind, d.name, e.name)

# you can call other methods within the class using self
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

z = Bag()
z.add(3)
print(z.data)
z.addtwice(5)
print(z.data)