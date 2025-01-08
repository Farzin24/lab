class BankAccount:
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited. Updated balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Updated balance: ₹{self.balance}")


account_number = input("Enter account number: ")
name = input("Enter account holder's name: ")
account_type = input("Enter account type (Savings/Current): ")
balance = float(input("Enter initial balance: "))
account = BankAccount(account_number, name, account_type, balance)


while True:
    print("\n1. Deposit\n2. Withdraw\n3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")

