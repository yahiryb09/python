# Lab 1 Part 2
sentence = input("Enter a sentence: ")
num = int(input("Enter the number of times to repeat the sentence: "))

sentence = sentence + "\n"

file = open("CompletedPunishment.txt", "a")

for i in range(num):
    file.write(sentence)
    
file.close()


