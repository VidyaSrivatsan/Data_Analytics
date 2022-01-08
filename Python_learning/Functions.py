
# define basic function

#def func1():
   # print("I am a function")

#func1()
# print(func1())
# print(func1)

# function that define an argument
# func2(arg1, arg2):
    #print(arg1, "", arg2)


# function that returns a value
#def cube(X):
    #return X*X*X

# function with default value for an argument
#def func3(x = 1, y =2):
   # return 1 + 2

#def power(num, x=1):
    #result = 1
    #for i in range(x):
        #result = result * num
   # return result

#func2(10,20)
#print(func2(10,20))
#print(cube(3))
#print(func3(1,2))
#print(power(2))
#print(power(2,3))

# Print total expense list of two individuals using function
def calculate_total_exp(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tom_exp_list = [2300, 4000, 3450]
tim_exp_list = [1245, 7890, 3289]

toms_total= calculate_total_exp(tom_exp_list)
tims_total= calculate_total_exp(tim_exp_list)

print("Toms total expense list is:", toms_total)
print("Tims total expense list is:", tims_total)



