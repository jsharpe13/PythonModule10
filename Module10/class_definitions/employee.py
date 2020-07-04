"""
Program: Employee.py
Author: Jacob Sharpe
Last date modified: 7/1/2020

The purpose of this program is to create an employee class
"""
import datetime


class Employee:
    """Employee Class """

    # Constructor
    def __init__(self, lname, fname, addr, pnum, sald, stdate, sal):
        self.last_name = lname
        self.first_name = fname
        self.address = addr
        self.phone_number = pnum
        self.salaried = sald
        self.start_date = stdate
        self.salary = sal

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, addr):
        self.address = addr

    def set_phone_number(self, pnum):
        self.phone_number = pnum

    def set_salaried(self, sald):
        self.salaried = sald

    def set_start_date(self, stdate):
        self.start_date = stdate

    def set_salary(self, sal):
        self.salary = sal

    def display(self):
        """ takes inputs and formats the string to return
        :return the formatted string employee information
         """
        if self.salaried == True:
            salaryquote = "Salaried employee: ${0:.0f}/year".format(self.salary)
        else:
            salaryquote = "Hourly employee: ${0:.2f}/hour".format(self.salary)

        d = self.start_date.strftime('%m-%d-%y')

        return self.first_name + " " + self.last_name + "\n" + self.address + "\n" + self.phone_number + "\n" + salaryquote + "\n" + "Start date: " + d

    def __str__(self):
        return 'Employee(last_name={}, first_name={},address={},phone_number={}, salaried={}, start_date={}, salary={}'.format(self.last_name,self.first_name,self.address,self.phone_number,self.salaried,self.start_date,self.salary)

    def __repr__(self):
        return 'Employee(last_name={}, first_name={},address={},phone_number={}, salaried={}, start_date={}, salary={}'.format(self.last_name,self.first_name,self.address,self.phone_number,self.salaried,self.start_date,self.salary)


if __name__ == '__main__':
    x = datetime.datetime(2019, 6, 28)
    emp = Employee('Patel', 'Sasha', '123 Main Street', '555-555-5555', True, x, 40000)  # call the constructor, needs to have a first and last name in parameter
    print(emp.display())  # display returns a str, so print the information

    del emp  # clean up!