import datetime
"""
Program: Person_Student.py
Author: Jacob Sharpe
Last date modified: 7//2020

The purpose of this program is to combine the student and person class
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
        return str(self.last_name) + ", " + str(self.first_name)


class Student:
    """Student class"""

    def __init__(self, maj, stdate, gpa=0.0, per=''):
        if not (isinstance(gpa, float)):
            raise ValueError
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError
        self.major = maj
        self.start_date = stdate
        self.gpa = gpa
        self.Person = per

    def change_major(self, maj):
        """ updates the major with the new information
        :param maj= the new major
        """
        self.major = maj

    def update_gpa(self, gpa):
        """ updates the gpa with the new information
        :param gpa - the new gpa
        """
        self.gpa = gpa

    def display(self):
        """ takes inputs and formats the string to return
        :return the formatted string student information
        """
        d = self.start_date.strftime('%m-%d-%y')
        return self.Person.display() + "\n" + "Major:" + self.major + "\n" + "start date:" + d + "\n" + "GPA:" + str(
            self.gpa)


# Driver
if __name__ == '__main__':
    person1 = Person("Johnson", "Mark")
    x = datetime.datetime(2021, 9, 28)
    student1 = Student("Computers", x, 4.0, person1)
    print(student1.display())
    student1.change_major("Being Awesome!")
    student1.update_gpa(3.0)
    print(student1.display())

    del person1  # clean up!
    del student1
