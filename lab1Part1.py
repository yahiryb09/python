# Lab 1 Part 1
import sys

addedSum = 0
userInput = input("Enter some numbers: ")
myList = userInput.split()
    
for x in myList:
    try:
        userInput = float(x)
    except ValueError:
        print("Error: Invalid number was entered")
        sys.exit()
        
if len(myList) < 2:
    # raise Exception("At least two numbers is required")
    print("Error: At least two numbers is required")
    sys.exit()


for x in range(len(myList)):
    myList[x] = float(myList[x])
    addedSum += myList[x]
    
if addedSum.is_integer():
    addedSum = int(addedSum)
    
print(addedSum)

# isalpha()
# if there is a space at the end of the user input