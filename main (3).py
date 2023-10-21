
class BankAccount:
   def__init__(self, account_number, account_holder_name,initial_balance=0.0);
self__account_number=self__account_number
self__account_balance=intial_balance
self__account_holder_name=account_holder_name
def deposit (self,amount):
  if amount>0:
    self__account_balance+=amount
    print(f"deposit ${amount:.2f}into account {self__account_number}")
  else:
    print("invalid deposit amount.please deposit a positive amount ")
    def withdraw (self, amount):
    if amount>0;
    if self__account_balance>=amount:
      self__account_balance-=amount
      print (f"withdraw ${amount:.2f} from account {self__account_number}")
    else:
      print("insufficient balance cannot withdraw ")
    else:
    print("invalid withdrawal amount please withdraw a positive ammount ")
    def display _balance(self):
    print("account{self__account_number} balance=${self__account_balance:.2f}")
    if__name-=="__main__":
    account 1=Bank Account ("123456","john doe",1000.0)
    account1.deposit(500.0)
    account1.withdraw(200.0)
    account1.display_balance()