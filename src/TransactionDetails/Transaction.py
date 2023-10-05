import datetime
class Transaction:
    trans_hist = []
    def __init__(self, transaction_id, source_account, destination_account, amount:float):
        self.transaction_id = transaction_id
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



    def get_transaction_details(self):
        return (f"Transaction ID: {self.transaction_id}\nSource Account: {self.source_account}\nDestination Account: {self.destination_account}\nAmount: ${self.amount:.2f}\nTimestamp: {self.timestamp}") 

    def get_transaction_history(account):
    history = []
    for transaction in transactions:
        if transaction.source_account == account or transaction.destination_account == account:
            history.append(transaction.get_transaction_details())
    return history