# what are objects
# A dog is an object but tommy(name of the dog) is an instance of the dog. The dog is called class.
#An adjective that describes "tommy" is property. For example, "My dog tommy is female"
#Female is an adjective and hence a property

# The actions that dog do are called "Methods".
# Object type or class = dog
# instance = name of dog "Tommy"
# Methods: Tommy barks. an action verb . Any action are methods. methods use parenthesis.
# properties: Female, that describes the dog.

# variables as object

# Anything you create is an object and will have properties and methods.

# object Methods and properties

# using variable objects methods and properties


#name = "John Deo"

#print(name.title())
#print(name.capitalize())
#print(name.isnumeric())
#print(name.split())
#print(name.replace('o', 'e'))
#print(len(name))

#Declare a variable and initialize
f = 0

#Global vs local variables in functions
def functions():
    global f
    f ="def"
    print(f)

functions()
print(f)

del f
print(f)