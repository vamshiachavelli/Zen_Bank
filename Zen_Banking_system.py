from random import randint

class Bank():
    def __init__(self) -> None:
        self.account_number = randint(100000,999999)
        self.First_Name = input("First Name = ")
        self.Last_Name = input("Last Name = ")
        self.Phone_number = int(input("Phone no = "))
        self.DOB = int(input("DOB(MM/DD/YY) = "))
        self.Gender = input("Gender = ")
        self.account_balance = 0

    def info(self):
        print(f"\nAccount_number = {self.account_number}")
        print(f"Fist_Name = {self.First_Name}")
        print(f"last_Name = {self.Last_Name}")
        print(f"Phone_number = {self.Phone_number}")
        print(f"DOB = {self.DOB}")
        print(f"Gender = {self.Gender}")
        print(f"Account_banlance = {self.account_balance}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.account_balance:
            print("Insufficient Funds")
        else:
            self.account_balance -= amount
            print("Successful Withdrawal")
            print(f"Current Account_Balance = {self.account_balance}")
    
    def deposit(self):
        amount = int(input("Enter amount to deposit = "))
        self.account_balance += amount
        print("Successful Deposit")
        print(f"Current Account_Balance = {self.account_balance}")

Accounts = []

def check_account_exist(account_no : int):
    global Accounts
    for account in Accounts:
        if account.account_number == account_no:
            return account
    return None
while True:
    print("\nWelcome to _____Bank")
    print("--------------------")
    print("1. Create Bank Account")
    print("2. Custome INFO")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer")
    print("6. Exit")
    option = int(input("Choice your option - "))
    print(f"---Your have choice option--- '{option}' ")
    if option == 1:
        Customer = Bank()
        Accounts.append(Customer)
    elif option ==2:
        if len(Accounts) == 0:
            print("No Accounts created.")
        else:
            for account in Accounts:
                account.info()
    elif option ==3:
        if len(Accounts) == 0:
            print("No Accounts created.")
        else:
            account_number = int(input("Enter Account_number = "))
            for search_account in Accounts:
                if search_account.account_number == account_number :
                    search_account.deposit()
                    search_account.info()
                    break
    elif option ==4:
        if len(Accounts) == 0:
            print("No Accounts created.")
        else:
            account_number = int(input("Enter Account_number = "))
            for search_account in Accounts:
                if search_account.account_number == account_number :
                    search_account.withdraw()
                    search_account.info()
                    break
    elif option ==5:
        sender_account = int(input("Enter sender account no = "))
        reciver_account = int(input("Enter reciver account no = "))
        sender_account_bank = check_account_exist(sender_account)
        reciver_account_bank = check_account_exist(reciver_account)
        if sender_account_bank != None and reciver_account_bank != None:
            amount_transfer = int(input("Enter amount to transfer = "))
            if amount_transfer <= sender_account_bank.account_balance:
                sender_account_bank.account_balance -=amount_transfer
                reciver_account_bank.account_balance += amount_transfer
                print("Transfer Sucessful")
                print(f"Sender balance = {sender_account_bank.account_balance}")
                print(f"reciver balance = {reciver_account_bank.account_balance}")
            else:
                print("insufficent funds")
        else:
            print("Account not found")
    elif option ==6:
        print("EXIT")
        break
    else:
        print("Invalid Option")