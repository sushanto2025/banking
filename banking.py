class Banking:
    def __init__(self,user_name,initial_balance):
        self.name=user_name
        self.balance=initial_balance

    def deposit(self,amount):
        if amount>0:
            self.balance +=amount
        return amount

    def get_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance -=amount
            return amount

ostad=Banking("Sushanto Halder",10000)
print(f"Account Name : {ostad.name}")
print(f"Account Balance : {ostad.balance} Taka")
print(f"Withdraw amount : {ostad.withdraw(1000)} Taka")
print(f"After Withdraw, Your Present Account Balance is: {ostad.get_balance()} Taka")
print(f"Deposit Amount : {ostad.deposit(2000)} Taka")
print(f"After Deposit, Your Present Account Balance is: {ostad.get_balance()} Taka")