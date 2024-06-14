from decimal import Decimal

class Calculations:
    history = []

    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    @staticmethod
    def addition(a: Decimal, b: Decimal) -> Decimal:
        return a + b

    @staticmethod
    def subtraction(a: Decimal, b: Decimal) -> Decimal:
        return a - b

    @staticmethod
    def multiplication(a: Decimal, b: Decimal) -> Decimal:
        return a * b
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        if b != 0:
            return a / b
        else:
            print("Error: Cannot divide by zero")

class History:
    
    historyOfCalculations = []

    #@classmethod
    #def add_history(cls, calculation):
    #    cls.history.append(calculation)

    #@classmethod
    #def get_history(cls):
    #    return cls.history

    @classmethod
    def record(historyOfCalculations, args):
        historyOfCalculations.append(args) 

    @classmethod
    def showHistory(historyOfCalculations):
        if historyOfCalculations == []:
            print("Nothing present in history")
        else:
            for item in historyOfCalculations:
                print(item)   