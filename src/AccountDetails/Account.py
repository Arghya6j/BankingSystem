
class Account():
    def __init__(self, account_number, customer, initial_balance: float = 0.0):
        self.account_number = account_number
        self.customer = customer  
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return(self.balance)
            
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
   
    def get_balance(self):
        return self.balance


