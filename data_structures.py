# reading this https://towardsdatascience.com/ultimate-guide-to-lists-tuples-arrays-and-dictionaries-for-beginners-8d1497f9777c
# lists
# a list is a mutable list of objects (all Python objects allowed) enclosed by square brackets
list_1 = ['head', 'ears', 5, [3, 1]]
print(list_1)
list_1.append('hands')
print(list_1)
list_1[1] = 'hair'
print(list_1)

# tuples
# immutable sequence of objects enclosed by parentheses
tuple_1 = (3, 'bags', 'belt', [2, 4])
print(tuple_1[3])

# arrays 
# arrays are not inbuilt, they need to be imported
# arrays are mutable sequences of the same data type (Ints, Floats, Characters)
import array as arr
arr_ints = arr.array('i', [1, 2, 3])
print(arr_ints)
arr_floats = arr.array('f', [1.4, 2.7, 3.3])
print(arr_floats)
arr_chars = arr.array('u', 'hello \u2641')
print(arr_chars)

# numpy arrays
# dictionaries
# a dictionary is an unordered (so not indexed) collection of key-pairs enclosed by curly braces
dict_1 = {'fruits': ['apple', 'grape'], 'number of fruits': 10, 'color': 'red'}
print(dict_1)
print(dict_1['fruits'])
print(dict_1['number of fruits'])
dict_1['number of fruits'] = 15
print(dict_1)
dict_1['price'] = 100
print(dict_1)
print(dict_1.keys())
print(dict_1.values())

# sets
# sets are unordered collections of unique objects enclosed by curly braces
# hence, these are used for removing duplicates
set_1 = {"apple", "banana", "cherry"}
print(set_1)
print(len(set_1))