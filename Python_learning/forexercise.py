# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0

# for h in result:
#      if h=="heads":
#         print("only heads", h)

#         count += 1

# print("The total number of time you got head is: ", count)

# pizza_toppings = ["Cheese", "Macroni", "Mushroom"]
# for toppings in pizza_toppings:
#     message = f"I would like my {toppings} on my pizza"
#     print(message)

# pizza_toppings = ["Cheese", "Macroni", "Mushroom"]

# def print_menu(toppings):
#     print("Welcome to julies pizzaria")
#     print("Our available toppings are:", (pizza_toppings))

# print_menu(pizza_toppings)

# for p in pizza_toppings:
#     if p == "Cheese":
#         print(p, ("free"))

#     else:
#         print(p, ("$1 extra"))


# def format_topping(topping):
#     for x in topping:
#        print(pizza_toppings)
#     if topping == "Cheese":
#         return "f{topping},(free)"
#     else:
#         return "f{topping},($1 extra)"

#print(pizza_toppings))




# numbers = [1, 2,3]
# square_numbers = []
# for n in numbers:
#     square_numbers.append(n**2)

# print(square_numbers)


# # Print square of all numbers between 1 to 10 except even numbers
# for i in range(1,11):
#     if i%2==0:
#      continue
#     print(i * i)

#Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 210, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

# month_list = ["January", "February", "March", "April", "May"]
# expense_list = [2340, 2500, 2100, 3100, 2980]
# e = input("Enter expense amount: ")
# e = int(e)

# month = -1
# for i in range(len(expense_list)):
#     if e == expense_list[i]:
#         month = i
#         break

# if month != -1:
#     print(f'You spent {e} in {month_list[month]}')
# else:
#     print(f'You didn\'t spend {e} in any month')

#program to print a table of number, say 5
# x = 5
# for a in range(1,11):
#     print(x, "X", a, "=", x * a )

# print sum of natural numbers between 1 to 7. Print the sum progressively

# sum = 0
# for x in range(1,8):
#     sum +=x
#     print("sum of natural numbers<=", x, "is:" , sum)

# print("sum of natural numbers<=", x, "is:" , sum)

# n = int(input("Enter a number"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# count = 0
# for i in range(1,10):
#     if i%2==0:
#         count +=1
#         print("The even numbers are:",i)

# print(f"we have {count} even numbers")