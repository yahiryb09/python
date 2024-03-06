# Lab 1 Part 3
textFileContents = ""
keyWord = input("Enter the key word you would like to search for: ")
keyWord = keyWord.lower()

file = open("PythonSummary.txt", "r")
textFileContents = file.read()

textFileContents = textFileContents.lower()

print("The word {0} occurs {1} times".format(keyWord, textFileContents.count(keyWord)))
        
        
file.close()
# print(results)