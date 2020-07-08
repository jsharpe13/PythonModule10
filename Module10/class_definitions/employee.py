"""
Program: Employee.py
Author: Jacob Sharpe
Last date modified: 7/1/2020

The purpose of this program is to create an employee class
"""

class Employee:
    """Employee Class """

    # Constructor
    def __init__(self, lname, fname, addr, pnum):
        self.last_name = lname
        self.first_name = fname
        self.address = addr
        self.phone_number = pnum

    def display(self):
        """ takes inputs and formats the string to return
        :return the formatted string employee information
         """
        return self.last_name + ", " + self.first_name + "\n" + self.address + "\n" + self.phone_number

    def __str__(self):
        return 'Employee(last_name={}, first_name={},address={},phone_number={})'.format(self.last_name,self.first_name,self.address,self.phone_number)

    def __repr__(self):
        return 'Employee(last_name={}, first_name={},address={},phone_number={})'.format(self.last_name,self.first_name,self.address,self.phone_number)