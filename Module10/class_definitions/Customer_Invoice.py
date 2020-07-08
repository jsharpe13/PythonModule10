"""
Program: Customer_Invoice.py
Author: Jacob Sharpe
Last date modified: 7/6/2020

The purpose of this program is to combine both customer and invoice classes
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
        return "Customer #" + str(
            self.customer_id) + ":" + self.last_name + ", " + self.first_name + "\n" + self.phone_number + "\n" + self.address


class Invoice:
    """Invoice Class """

    def __init__(self, iid, cust=''):
        self.invoice_id = iid
        self.items_with_price = {}
        self.Customer = cust

    def add_item(self, item):
        """ adds item to the dictionary
         :param item
        """
        self.items_with_price.update(item)

    def create_invoice(self):
        """ takes dictonary and outputs the totals of items purchased and Customer class
        """
        sum = 0
        tax_rate = 0.06
        tax = 0
        sum_with_tax = 0

        print(self.Customer.display())

        for key, value in self.items_with_price.items():
            sum = sum + value
            print(key + ".....$" + str(value))

        tax = sum * tax_rate
        sum_with_tax = sum + tax
        print("Tax.....${:.2f}".format(tax))
        print("Total.....${:.2f}".format(sum_with_tax))


# Driver
if __name__ == '__main__':
    captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones in the verse', 'Firefly, somewhere in the verse')
    invoice = Invoice(1, captain_mal)
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
