class Payment:
    def __init__(self, amount, transaction_id, status):
        self.amount = amount
        self.transaction_id = transaction_id
        self.status = status
    
    def validate(self):
        print("Payment Processing")
    
    def create_payment(self):
        print(f"The payment for {self.amount} is created by the {self.transaction_id} and the status is {self.status}")
    
    def make_payment(self, amount, status):
        print(f"The payment for {amount} is done. The transaction id is {self.transaction_id} and the status is {status}")
    

class UpiPayment(Payment):
    def __init__(self,  amount, transaction_id, status, upi_id):
        super().__init__(amount, transaction_id, status)
        self.upi_id = upi_id

    def validate(self):
        super().validate()
        print("Redirecting to UPI")


p = Payment(2000, 456665, "PENDING")
p.create_payment()
p.make_payment(2000, "SUCCESS")


u = UpiPayment(2000, 5526, 456665, "PENDING")
u.validate()