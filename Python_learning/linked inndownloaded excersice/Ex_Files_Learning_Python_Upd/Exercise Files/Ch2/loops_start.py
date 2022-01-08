#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
# while(x < 5):
#       print(x)
#       x = x + 1

  # define a for loop
for x in range(5, 10):
      print(x)

  # use a for loop over a collection
weeks = ["Mon", "Tues", "Wed", "Thurs", "Frid", "Sat", "Sun"]
w = weeks
print(w)

  # use the break and continue statements
for x in range(5, 10):
      # if x==7:
      #       break
      # else:
        if x%2==0:
          continue
        print(x)


  #using the enumerate() function to get index
weeks = ["Mon", "Tues", "Wed", "Thurs", "Frid", "Sat", "Sun"]
for i,w in enumerate(weeks):
   print(i,w)

if __name__ == "__main__":
  main()
