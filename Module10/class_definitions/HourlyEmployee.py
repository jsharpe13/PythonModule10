"""
Program: HourlyEmployee.py
Author: Jacob Sharpe
Last date modified: 7/7/2020

The purpose of this program is to create a derived employee class
"""
from class_definitions.employee import Employee
import datetime


class HourlyEmployee(Employee):
    """Hourly Derived class"""

    def __init__(self, lname, fname, addr, pnum, stdate, hpay):
        super().__init__(lname, fname, addr, pnum)
        self.start_date = stdate
        self.hourly_pay = hpay

    def display(self):
        """ takes inputs and formats the string to return
        :return the formatted string employee information
        """
        st_date = self.start_date.strftime('%m-%d-%Y')
        return super().display() + "\n" + "Start Date: " + str(st_date) + "\n" + "pay: ${0:.2f}".format(self.hourly_pay) + " an hour"

    def give_raise(self, change):
        """ changes the hourly pay
        :param change- the changed hourly pay
        """
        self.hourly_pay = change

    def __str__(self):
        return super().str() + "HourlyEmployee(start_date={}, hourly_pay={}".format(self.start_date, self.hourly_pay)

    def __repr__(self):
        return super().str() + "HourlyEmployee(start_date={}, hourly_pay={}".format(self.start_date, self.hourly_pay)


# Driver
if __name__ == '__main__':
    date = datetime.datetime(2020, 7, 7)
    hour_emp = HourlyEmployee("Sharpe", "Jacob", "123 Main Street", '555-555-5555', date, 10.00)
    print(hour_emp.display())
    hour_emp.give_raise(12.00)
    print(hour_emp.display())

    del hour_emp