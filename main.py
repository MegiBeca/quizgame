print("Hello!!")
originalPrice = float(input("Enter the original cost of the item: "))
salePrice = float(input("Enter the sale price: "))
percentOff = int((originalPrice - salePrice)/originalPrice * 100)
print("Original price: $", format(originalPrice, ".2f"), sep="")
print("Sale price: $", format(salePrice, ".2f"), sep="")
print("Percent off: ", format(percentOff, "d"),"%", sep="")
if(percentOff >= 50):
    print("You got a great sale!")

originalPrice = input(" Enter the original price of the item: ")
price = int(originalPrice)
if price >= 50:
    print("You did not get a sale.")
else:
    print("You got a sale")

price = int(input("Enter your price: "))
if price >= 40:
    print("You did not get a sale.")
else:
    if price <=30:
        print("You got a sale.")
    else:
        print("Normal Price")

name = input("Enter your favorite icecream flavor: ")
x = 0
while(x<20):
    print(name)
    x=x+1

name = input("Enter your favorite icecream flavor: ")
for x in range (20):
    print(name)

for x in range(5) :
    print(x, end=" ")

for x in range(1,5):
		   print(x, end=" ")
for x in range(3,20,2):
	 	   print(x, end=" ")
numIterations = 6
for x in range(numIterations):
	print(x, end=" ")
numIterations = 6
for x in range(1, numIterations+1):
    print(x, end=" ")
name = input("What is your name: ")
for x in range(6):
    for x in range(3):
        print(name + " ", end=" ")
    print()

height = int(input("Enter height: "))
for row in range(1, height+1):
    for column in range(row):
        print(row, end=" ")
    print()
doAgain = True
while doAgain:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number:"))
    num3 = int(input("Enter third number:"))
    num4 = int(input("Enter fourth number:"))
    maxNum1 = max(num1, num2, num3, num4)
    print("The largest of the fourth numbers is:", maxNum1)
    another = input("Type 'y' to find another max number "+" or any other key to quit.")
    if another != 'y':
        doAgain = False
print("Done")