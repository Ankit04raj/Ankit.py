# creat account class with 2 attributes- balance 7 account no.
# creat method for debit,credit & printing the balance

class Account:
    def __init__(self,bal , acc):
        self.balance = bal
        self.account_no = acc
    
    #DEBIT METHOD:-
    def debit(self,amount):
        self.balance -= amount
        print("Rs." , amount ,"was debited")
        print("total balance = ",self.get_balance())

    #CREDIT METHOD:-
    def credit(self,amount):
        self.balance += amount
        print("Rs." , amount ,"was credited")
        print("total balance = ",self.get_balance())

    #FINAL BALANCE
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,57898896)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(30000)
