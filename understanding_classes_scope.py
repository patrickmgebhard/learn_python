"""
-notes on https://docs.python.org/3/tutorial/classes.html
-classes allow to bundle data (properties) and functionality (methods); creating a new class creates a new type of object, then you can create new instances of that object
-child classes inherit methods from their parents
    => what about properties 
-a namespace is a mapping of a name to an object e.g. planet = "Earth"; the basic question is which value will be taken in the script when use the variable planet
-there is the local (created when the function is called and deleted when the function returns or raises an exception), nonlocal and global namespaces 
"""
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam 
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    # this outputs "test spam" because "local spam" is only locally within the do_local() function bound to the variable
    print("After local assignment: ", spam)
    do_nonlocal()
    # this outputs "nonlocal spam" because spam is nonlocally bound so not only in the function, hence "test spam" is overwritten by "nonlocal spam"
    print("After nonlocal assignment: ", spam)    
    do_global()
    # this outputs "nonlocal spam", because the variable is nonlocally bound to "nonlocal spam" and that namespace is searched first and then resolved
    print("After global assignment: ", spam)

scope_test()
# this outputs "global spam", because it uses the global scope; the nonlocal scope of scope_test is only available within the function; if you remove the do_global() call you'll see that spam is not defined on a global scope
print("In global scope: ", spam)