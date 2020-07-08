"""
Program: Derived_Student_Person.py
Author: Jacob Sharpe
Last date modified: 7/6/2020

The purpose of this program is to combine the student and person class using inheritance
"""


class Person:
    """Person class using class Address, Class Composition"""

    def __init__(self, lname, fname):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname

    def display(self):
        """ takes inputs and formats the string to return
        :return the formatted string Person information
        """
        return str(self.last_name) + ", " + str(self.first_name)


class Student(Person):

    def __init__(self, stu_id, lname, fname, maj='Computer Science', gpa='0.0'):
        super().__init__(lname, fname)
        self.student_id = stu_id
        self.major = maj
        self.gpa = gpa

    def display(self):
        """ takes inputs and formats the string to return
        :return the formatted string student information
        """
        return super().display() + ":(" + str(
            self.student_id) + ") " + self.major + " gpa: " + str(self.gpa)


# Driver
if __name__ == '__main__':
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student
