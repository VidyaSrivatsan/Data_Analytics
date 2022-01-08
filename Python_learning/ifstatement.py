# Use If else statement to find out whether the number is odd or even
#num=input("Enter a number:")
#num=int(num)
#if num%2==0:
    #print("The number is even")

#else:
    #print("The Number is odd")

#Write a programm that ask user to enter a dish name and should print which cuisine is that dish

# Indian=["dal", "Samosa", "Bhaji"]
# chinese=["pasta", "Momos", "eggrole"]
# italian=["pizza", "Pasta"]

# dish=input("Enter a dish name:")


# if dish in Indian:
#     print("The cuisine is Indian")

# elif dish in chinese:
#     print("The dish is chinese")

# elif dish in italian:
#     print("The dish is italian")

# else:
#     print("The dish is neither Indian nor mexican nor chinese")

# ## Exercise: Python If Condition
# # 1. Using following list of cities per country,
# #     ```
# #     india = ["mumbai", "banglore", "chennai", "delhi"]
# #     pakistan = ["lahore","karachi","islamabad"]
# #     bangladesh = ["dhaka", "khulna", "rangpur"]
# #     ```
# # Write a program that asks user to enter a city name and it should tell which country the city belongs to

# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# city=input("Enter a city name:")

# if city in india:
#     print("This city is in India:")

# elif city in pakistan:
#     print("This city is in pakistan:")

# elif city in bangladesh:
#     print("The city is in bangladesh:")

# else:
#     print("The city is in a different country" )

# #Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# # For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# city1=input("Enter a city name:")
# city2=input("Enter another city name:")

# if city1 in india and city2 in india:
#     print("Both cities are in India")

# else:
#     print("They do not belong to same country" )

# # Write a python program that can tell you if your sugar is normal or not.
# #  Normal fasting level sugar range is 80 to 100.
# #     1. Ask user to enter his fasting sugar level
# #     2. If it is below 80 to 100 range then print that sugar is low
# #     3. If it is above 100 then print that it is high otherwise print that it is normal

# sugar=input("Enter your fasting sugar level:")
# sugar = float(sugar)
# if sugar<80:
#     print("sugar is low")
# elif sugar>100:
#     print("sugar is high")
# else:
#     print("Your sugar is normal")

# x=y=z=0

# largest=x
# x = float(input("Enter first number"))
# y = float(input("Enter second number"))
# z = float(input("Enter third number"))

# if y> largest:
#     largest = y
# if z> largest:
#     largest = z
#     print("The largest number is:",largest)

# x = y = z = 0
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input(" Enter third number: "))
# sum1 = sum2 = 0
# sum1 = x + y + z

# if x== y and z!=x:
#     sum2 +=z
# else:
#     if x==z:
#         sum2 +=y
#     else:
#         if y==z:
#             sum2 +=x
#         else:
#             sum2 += x + y + z
# print("The numbers are", x, y, z)
# print("The sum of first, second and third number is", sum1)
# print("The sumb of non duplicate number is", sum2)

radius = float(input("Enter radius of the circle: "))


choice = int(input("Enter your choice: "))
if choice==1:
    area = 3.14 * radius * radius
    print("Area of circle is: ", area)
else:
    Perimeter = 2 * 3.14 * radius
    print("Area of perimeter is: ", Perimeter)







