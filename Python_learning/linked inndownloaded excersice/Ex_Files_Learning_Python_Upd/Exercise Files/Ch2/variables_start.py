#
# Example file for variables
#

# Declare a variable and initialize it
f = 0
#print(f)


# # re-declaring the variable works
# f = "prashant"
# print(f)



# # ERROR: variables of different types cannot be combined
# f = "soup"
# g = 123
# print (f + str(g))


# Global vs. local variables in functions
def somefunct():
    global f
    f = "def"
    print(f)

somefunct()
print(f)


