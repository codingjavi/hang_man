print ("Student 1")

class Student(object):
    def __init__(self, first_name, last_name, grade_level, school):
        self.first_name = first_name
        self.last_name = last_name
        self.grade_level = grade_level
        self.school = school
        print (first_name + " " + last_name + " " + str(grade_level) + " " + school)

student_first_name = input("Enter First Name: ")
student_last_name = input("Enter Last Name: ")
student_grade = input("Enter Grade Level: ")
student_school = input("Enter School: ")

Student1 = Student(student_first_name, student_last_name, student_grade, student_school)

print (Student1)

