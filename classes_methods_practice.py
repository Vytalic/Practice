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
        
                    
    def wrong_pin(self):
        print("\nError: You have entered an incorrect pin too many times. Exiting...\n")
        return False
    
    
    def check_pin(self):
        attempts = int(0)
        for attempt in range(5):            
            if attempts > 0 and attempts != 5:
                print(f"\nYou will be locked out after {5 - attempts} more tries.", end='')
            code = int(input("\nEnter your pin: "))
            if code == self.pin:
                return True
            elif code != self.pin:
                attempts += 1
                if attempts == 5:
                    return False
                 
            
    def check_balance(self):
        check_pin = self.check_pin()
        if check_pin == True:
            print("\n------------------------")
            print(f"Welcome {self.owner}!")
            print(f"Your balance is {self.balance}")
            print("------------------------")
        else:
            self.wrong_pin()
    
    
    def withdraw(self):
        check_pin = self.check_pin()
        if check_pin == True:
            print(f"\nWelcome {self.owner}!")
            withdraw_x = int(input("Withdraw amount: "))
            previous_bal = self.balance
            self.balance -= withdraw_x
            print("\n\n----------------------------------------")
            print("---------------Receipt------------------")
            print("----------------------------------------")
            print(f"-Owner: {self.owner}                      ")
            print(f"-Account Number: {self.acct_num}                ")
            print("-                                      ")
            print(f"-Previous Balance: {previous_bal}                ")
            print(f"-Withdrawal: {withdraw_x}                        ")
            print(f"-New Balance: {self.balance}                     ")
            print("----------------------------------------\n\n")
        else:
            self.wrong_pin()


    def deposit(self):
        check_pin = self.check_pin()
        if check_pin == True:
            print(f"\nWelcome {self.owner}!")
            deposit_x = int(input("Deposit amount: "))
            previous_bal = self.balance
            self.balance += deposit_x
            print("\n\n----------------------------------------")
            print("---------------Receipt------------------")
            print("----------------------------------------")
            print(f"-Owner: {self.owner}                      ")
            print(f"-Account Number: {self.acct_num}                ")
            print("-                                      ")
            print(f"-Previous Balance: {previous_bal}                ")
            print(f"-Deposit: {deposit_x}                        ")
            print(f"-New Balance: {self.balance}                     ")
            print("----------------------------------------\n\n")
        else:
            self.wrong_pin()

acct1 = Bank("Ben Clark", 222333, 7777, 1000, 0.025)
done = False
user_acct_num = int(input("\nPlease enter your account number: "))
while done == False:
    print("\n----------Menu----------")
    print("------------------------")
    print("1) Check Balance")
    print("2) Withdraw")
    print("3) Deposit")
    print("4) Exit")
    print("------------------------")
    user_choice = int(input("\nChoose an option from above: "))
    
    if user_choice == 1:
        acct1.check_balance()
    elif user_choice == 2:
       acct1.withdraw()
    elif user_choice == 3:
        acct1.deposit() 
    elif user_choice == 4:
        done = True













# Student - name, age, and grade level
# add/remove courses - calculating gpa




# Employee - name, position, salary
# giving raises - calculating taxes




# Car - make, model, and year
# starting - stopping - accelerating - check fuel level




# Contact - names, phone number, and email address
# add/remove contacts - search for contacts by name/phone number