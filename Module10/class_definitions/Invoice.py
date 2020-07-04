"""
Program: Invoice.py
Author: Jacob Sharpe
Last date modified: 7/2/2020

The purpose of this program is to create an Invoice class
"""

class Invoice:
    """Invoice Class """

    def __init__(self, iid, cid, lname, fname, pnum, addr):
        self.invoice_id = iid
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnum
        self.address = addr
        self.items_with_price = {}

    def add_item(self, item):
        """ adds item to the dictionary
         :param item
        """
        self.items_with_price.update(item)

    def create_invoice(self):
        """ takes dictonary and outputs the totals of items purchased
        """
        sum = 0
        tax_rate = 0.06
        tax = 0
        sum_with_tax = 0

        for key, value in self.items_with_price.items():
            sum = sum + value
            print(key + ".....$" + str(value))

        tax = sum * tax_rate
        sum_with_tax = sum + tax
        print("Tax.....${:.2f}".format(tax))
        print("Total.....${:.2f}".format(sum_with_tax))

    def __str__(self):
        pass

    def __repr__(self):
        pass


# Driver
if __name__ == '__main__':
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()

    del invoice #Clean up
