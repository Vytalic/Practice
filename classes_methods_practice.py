# More practice with Classes and Class methods
# Used chatGPT to facilitate ideas regarding what kind of classes to make





# Bank Account
# deposit - withdraw - check balance

class Bank():
    def __init__(self, owner, acct_number, pin, balance, interest_rate):
        self.owner = owner
        self.acct_num = acct_number
        self.pin = pin
        self.balance = balance
        self.interest_rate = interest_rate
        
    def check_balance(self):
        return(self.balance)
    
    def withdraw(self):
        withdraw_x = int(input("\nWithdraw amount: "))
        previous_bal = self.balance
        self.balance += withdraw_x
        print("\n\n----------------------------------------")
        print("---------------Receipt------------------")
        print("----------------------------------------")
        print(f"-Owner: {self.owner}                      ")
        print(f"-Account Number: {self.acct_num}                ")
        print("-                                      ")
        print(f"-Previous Balance: {previous_bal}                ")
        print(f"-Withdrawal: {withdraw_x}                        ")
        print(f"-New Balance: {self.balance}                     ")
        print("----------------------------------------")

acct1 = Bank("Ben Clark", "222333", 7438, 1000, 0.025)
acct1.withdraw()

# Student - name, age, and grade level
# add/remove courses - calculating gpa




# Employee - name, position, salary
# giving raises - calculating taxes




# Car - make, model, and year
# starting - stopping - accelerating - check fuel level




# Contact - names, phone number, and email address
# add/remove contacts - search for contacts by name/phone number