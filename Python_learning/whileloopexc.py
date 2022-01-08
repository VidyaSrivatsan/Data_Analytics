# program to calculate and print the sums of evne and odd intergers of the first n natural numbers
# n = int(input("upto which natural number?: "))
# x =1
# sum_even=sum_odd = 0
# while x<=n:
#     if x%2==0:
#         sum_even +=x
#     else:
#         sum_odd +=x
#     x +=1

# print("The sum of even interger is:", sum_even)
# print("The sum of odd interger is:", sum_odd)

# count = sum = 0
# ans = "y"
# while ans=="y":
#     n = int(input("Enter number: "))
#     if n<0:
#        print("Thenumber entered is below zero. Abort")
#     break
#     sum = sum + n
#     count +=1
#     ans=input("want to enter more number (y/n): ")

# else:
#        print("Your entered number so far is: ", count)

# print("The sum of the number is:", sum)

n = int(input("Enter multiple of 7: "))

while n%7 != 0:
    n = int(input("Enter multiple of 7"))
else:
    print(f"{n} is a multiple of 7")





