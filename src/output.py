from CustomerDetails.Customer import Customer
from AccountDetails.Account import Account
from TransactionDetails.Transaction import Transaction




if __name__== "__main__":
    Customer1 = Customer("C001", "John Doe", "123 Main St", "555-1234")
    Customer2= Customer("C002", "Jane Smith", "456 Elm St",  "555-5678")
    

    print("Customer-Details",Customer1.get_customer_info())
    print("Customer-Details",Customer2.get_customer_info())


    john_savings = Account("CZ001", Customer1.name)
    john_checking = Account("SZ001", Customer1.name)
    jane_savings = Account("CZ002", Customer2.name)
    jane_checking = Account("SZ002", Customer2.name)
    
    
    print(john_savings.deposit(1000),"$","Deposited to john_savings account")
    print(jane_checking.withdraw(200),"$","withdrawl from johns_checking Account")
    print(jane_checking.deposit(2000),"$","withdrawl from johns_checking Account")

    transfer_amount = 300
    if john_checking.withdraw(transfer_amount)==True:
        jane_savings.deposit(transfer_amount)
    else:
        print("Low Balance Service not available")

    print(f"John Doe's Savings Account Balance- ${john_savings.get_balance()}")
    print(f"John Doe's Checking Account Balance- ${john_checking.get_balance()}")
    print(f"Jane Smith's Savings Account Balance- ${jane_savings.get_balance()}")
    print(f"Jane Smith's Checking Account Balance- ${jane_checking.get_balance()}")
    
    
    transactions1=Transaction("Tr001", john_savings, None, 1000)
    transactions2=Transaction("Tr002", None, jane_checking, 200)
    transactions3=Transaction("Tr003", john_checking, jane_savings, transfer_amount,)

    
    print("Total_Transaction_Details:",transactions1.get_transaction_details())
    print("Total_Transaction_Details:",transactions2.get_transaction_details())
    print("Total_Transaction_Details:",transactions3.get_transaction_details())

    Trans=[]
    print(Trans.append(f"Transaction ID: {self.transaction_id}\nSource Account: {self.source_account}\nDestination Account: {self.destination_account}\nAmount: ${self.amount:.2f}\nTimestamp: {self.timestamp}")) 
    return Trans