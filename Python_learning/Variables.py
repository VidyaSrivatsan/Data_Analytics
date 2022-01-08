# What are variable?

# Variable stores a piece of information and can be resued.

# Calculating the area


width = 10

height = 5

area = width * height

print(area)
print(type(width), type(height))

first_name = "Alia"
last_name = "Bhat"
Age = 20
Weight = 60.5
is_minor = False

print(first_name, type(first_name))
print(is_minor, type(is_minor))

#python takes all decimal point as float
print(Weight, type(Weight))

# Run a program to check if a couch will fit the area

width = int(input("Enter the width in feet:"))
length = int(input("enter the length in feet:"))

area = width*length
# the area-needed is a constant and is not hard-coded. python does not have a constant type.hence
# variable is used.
area_needed = 100
couch_will_fit = (area>area_needed)

print("Area is:", area)
#conditins returns a boolean value.
print("is the area large enough?", couch_will_fit)



