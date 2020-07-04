"""
Program: Customer.py
Author: Jacob Sharpe
Last date modified: 7/3/2020

The purpose of this program is to create a Student class
"""


class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(
                major)):
            raise ValueError
        if not (isinstance(gpa, float)):
            raise ValueError
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def display(self):
        """ takes inputs and formats the string to return
         :return the formatted string student information
         """
        return self.last_name + " " + self.first_name + ", major:" + self.major + ", GPA:" + str(self.gpa)


# Driver
# Valid student
student1 = Student('Johnson', 'Mark', 'Computers')
print(student1.display())
# Valid student
student2 = Student('Richards', 'Simon', 'Computers', 3.5)
print(student2.display())
# Invalid student
# Wait! try/except needed!
try:
    student3 = Student('123', 'Mark', 'Computers', 3.5)
except ValueError:
    print("Error found, person not created")
