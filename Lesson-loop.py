# i = 1
# while i < 6:
#   print(i)
#   i += 1

# print("1")
# print("2")
# print("3")
# print("4")
# print("5")
# print("6")
print("Please enter a number for the table")
tableNumber = int(input())
print("Please enter a range of the table")
count = int(input())

# 5 x 1 = 5
index = 1
while index <= count:
    print("%d x %d = %d" %(tableNumber, index, index * tableNumber))
    index = index + 1
#print(str(tableNumber) + " x " + str(index) + " = " + str(index * tableNumber))