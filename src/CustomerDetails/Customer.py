class Customer():
    def __init__(self, customer_id, name, address, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
    def get_customer_info(self):
        return(f"Customer ID: {self.customer_id}\n Name: {self.name}\nAddress: {self.address}\nPhone_Number:{self.phone_number}" )  

