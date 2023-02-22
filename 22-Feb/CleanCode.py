'''Single Responsibility Principle

This Class has 4 responsibilities i.e. Adding,Subtracting,Multiplying and Division'''

'''class Calculator:
    def add(self, x, y):
        return x+y

    def subtract(self, x, y):
        return x-y

    def multiply(self, x, y):
        return x*y

    def division(self, x, y):
        return x/y'''

# We can divide this class into 4 different classes


class Adder:
    def add(self, x, y):
        return x+y


class Subtracter:
    def subtract(self, x, y):
        return x-y


class Multiplier:
    def multiply(self, x, y):
        return x*y


class Divider:
    def divide(self, x, y):
        return x/y

# Now we can make one class Calculator which is responsible for managing the functionality of these 4 classes


class Calculator:
    def __init__(self):
        self.adder = Adder()
        self.subtracter = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()

    def add(self, x, y):
        return self.adder.add(x, y)

    def subtract(self, x, y):
        return self.subtracter.subtract(x, y)

    def multiply(self, x, y):
        return self.multiplier.multiply(x, y)

    def divide(self, x, y):
        return self.divider.divide(x, y)


'''Open/Closed Principle'''


class Handler():
    def process_payment(self, payment):
        pass


class CreditCardHandler(Handler):
    def process_payment(self, payment):
        # Handle Credit Card Payments
        pass


class DebitCardHandler(Handler):
    def process_payment(self, payment):
        # Handle Debit Card Payments
        pass


class UPIHandler(Handler):
    def process_payment(self, payment):
        # Handle UPI Payments
        pass


class PaymentProcessor():
    def __init__(self):
        self.handlers = {}

    def register_handler(self, payment_type, handler):
