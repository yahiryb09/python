# Lab 1 Part 5
import json

run = 0

while(run != 6):
    print("Select an option:")
    print("(1) Add Student")
    print("(2) Checks Student Grade")
    print("(3) Edit Student's Grade")
    print("(4) Delete Student's Grade")
    print("(5) Print All Grades")
    print("(6) Quit")
    run = int(input())
    
    if run == 1:
        with open('grades.txt') as file:
            data = json.load(file)
        file.close()
        
        student = input("Enter Student Name: ")
        grade = float(input("Enter Student Grade: "))
        data[student] = grade
        # x = json.dumps(y)
        
        file = open("grades.txt", "w")
        json.dump(data, file)
        file.close()
    elif run == 2:
        with open("grades.txt") as file:
            y = json.load(file)
        
        student = input("Enter Student Name: ")
        print("Grade: {}".format(y[student]))
        print("\n")
        file.close()
    elif run == 3:
        with open('grades.txt') as file:
            data = json.load(file)
        file.close()
        
        student = input("Enter Student Name: ")
        
        if student in data:
            grade = float(input("Enter Student Grade: "))
            data[student] = grade
            # x = json.dumps(y)
            
            file = open("grades.txt", "w")
            json.dump(data, file)
            file.close()
        else:
            print("Error: Student does not exist")
    elif run == 4:
        with open('grades.txt') as file:
            data = json.load(file)
        file.close()
        
        student = input("Enter Student Name: ")
        
        if student in data:
            data[student] = None
            # del(data[student])
            # # x = json.dumps(y)
            
            file = open("grades.txt", "w")
            json.dump(data, file)
            file.close()
        else:
            print("Error: Student does not exist")
    elif run == 5:
        with open('grades.txt') as file:
            data = json.load(file)
        file.close()
        
        print(data)
        
        