print ("Student 1")
class Student(object):
    def __init__(self, first_name, last_name, grade_level, school):
        self.first_name = first_name
        self.last_name = last_name
        self.grade_level = grade_level
        self.school = school
        print (first_name + " " + last_name + "is in grade "+ str(grade_level) + " at " + school)

class StudentWithNoSchool(object):
    def __init__(self, first_name, last_name, grade_level):
        self.first_name = first_name
        self.last_name = last_name
        self.grade_level = grade_level
        if int(grade_level) >= 9:
            school = "High School"
        elif int(grade_level) >= 7:
            school = "Middle School"
        elif int(grade_level) >= 1:
            school = "Elementary School"
        print (first_name + " " + last_name + " " + "is in grade " + str(grade_level) + " in " + school)
        
student_first_name = input("Enter First Name: ")
student_last_name = input("Enter Last Name: ")
student_grade = input("Enter Grade Level: ")
student_school = input("Enter School: ")

Student1 = Student(student_first_name, student_last_name, student_grade, student_school)
print ("Student 2")
student_first_name = input("Enter First Name: ")
student_last_name = input("Enter Last Name: ")
student_grade = input("Enter Grade Level: ")


Student2 = StudentWithNoSchool(student_first_name, student_last_name, student_grade)


