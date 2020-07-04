"""
Program: Customer.py
Author: Jacob Sharpe
Last date modified: 7/2/2020

The purpose of this program is to create a customer class
"""


class Customer:
    """Customer Class """

    def __init__(self, cid, lname, fname, pnum, addr):
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnum
        self.address = addr
        x = isinstance(self.customer_id, int)
        # Constructor raised the Attribute Error not the display()
        if not x:
            raise AttributeError("'Customer' object has no attribute 'cid'")

    def display(self):
        """ takes inputs and formats the string to return
        :return the formatted string customer information
        """
        return self.first_name + " " + self.last_name + ":" + str(
            self.customer_id) + "\n" + self.address + "\n" + self.phone_number

    def __str__(self):
        pass

    def __repr__(self):
        pass


# Driver
if __name__ == '__main__':
    customer1 = Customer(12345, 'Glass', 'Mark', '555-555-5555', '123 Main Street')
    print(customer1.display())
    customer2 = Customer('12345', 'Glass', 'Mark', '555-555-5555', '123 Main Street')
    print(customer1.display())

    del customer1  # clean up!
    del customer2
