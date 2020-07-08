"""
Program: SalariedEmployee.py
Author: Jacob Sharpe
Last date modified: 7/7/2020

The purpose of this program is to create a derived employee class
"""
from class_definitions.employee import Employee
import datetime


class SalariedEmployee(Employee):
    """Salaried Derived class"""

    def __init__(self, lname, fname, addr, pnum, stdate, sal):
        super().__init__(lname, fname, addr, pnum)
        self.start_date = stdate
        self.salary = sal

    def display(self):
        """ takes inputs and formats the string to return
        :return the formatted string employee information
        """
        st_date = self.start_date.strftime('%m-%d-%Y')
        return super().display() + "\n" + "Start Date: " + str(st_date) + "\n" + "pay: ${0:,}".format(
            self.salary) + " a year"

    def give_raise(self, change):
        """ changes the salary pay
        :param change- the changed salary pay
        """
        self.salary = change

    def __str__(self):
        return super().str() + "SalariedEmployee(start_date={}, salary={}".format(self.start_date, self.salary)

    def __repr__(self):
        return super().str() + "SalariedEmployee(start_date={}, salary={}".format(self.start_date, self.salary)


# Driver
if __name__ == '__main__':
    date = datetime.datetime(2020, 7, 7)
    sal_emp = SalariedEmployee("Sharpe", "Jacob", "123 Main Street", '555-555-5555', date, 40000)
    print(sal_emp.display())
    sal_emp.give_raise(45000)
    print(sal_emp.display())

    del sal_emp
