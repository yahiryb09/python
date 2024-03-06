# Lab 1 Part 4
class Courses:
    num = 0
    def __init__(self, department, number, name, credits, lecture_days, start_time, end_time, average_grade):
        self.department = department
        self.number = number
        self.name = name
        self.credits = credits
        self.lecture_days = lecture_days
        self.start_time = start_time
        self.end_time = end_time
        self.average_grade = average_grade
        Courses.num += 1

    def displayCourseInfo(self):
        print("COURSE {}: {}{}: {}".format(Courses.num, self.department, self.number, self.name))
        print("Number of Credits: {}".format(self.credits))
        print("Days of Lectures: {}".format(self.lecture_days))
        print("Lecture Time: {} - {}".format(self.start_time, self.end_time))
        print("Stat: on average, students get {}% in this course\n".format(self.average_grade))
        
file = open("classesInput.txt", "r")
numCourses = file.readline().strip("\n")
numCourses = int(numCourses)

listOfCourses = []

for i in range(numCourses):
    course = Courses(file.readline().strip("\n"), file.readline().strip("\n"), file.readline().strip("\n"), file.readline().strip("\n"), file.readline().strip("\n"), file.readline().strip("\n"), file.readline().strip("\n"), file.readline().strip("\n"))
    course.displayCourseInfo()
    listOfCourses.append(course)


file.close()