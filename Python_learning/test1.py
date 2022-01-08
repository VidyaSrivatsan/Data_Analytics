# import modules.test as t
# area = t.cal_squ_area(6)
# print(area)

# area1 = t.cal_tri_area(6,8)
# print(area1)


result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == "heads":
        count += 1
print("Heads count: ",count)
