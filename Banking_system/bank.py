class BankAccount:
     def __init__(self, account_number,account_holder,balance, loan_balance):
          self.account_number = account_number
          self.account_holder = account_holder
          self.balance = balance
          self.transaction_history = []
          self.loan_balance = loan_balance
          
     def view_balance(self):
         print(f"Account balance is : {self.balance}")    
          
     def deposit(self, amount):
          self.balance += self.amount
          self.transaction_history.append("deposit {self.amount}") 
          print(f"deposite amount {self.amount}")
          
     def withdraw(self, amount):
         if self.balance >= self.amount:
                self.balance -= self.amount
                self.transaction_history.append("withdraw {self.amoutn}")
                print(f"Withdraw {self.amount}") 
                
     def view_transaction_history(self):
         for i, transaction in enumerate(self.transaction_history):   
           print(f"transaction id {i} : {transaction}")  
           
    #  def apply_for_loan(self,amount, interest_rate, term_years): 
    #      loan_amount = principal*(1+self.interest_rate)*self.term_years     
                       
          
     def view_loan_balance(self):
         print(f"Loan balance is {self.loan_balance}") 
         
         
class Banking_system:
    def __init__(self):
        self.accounts = [] 
        
        
    def create_account(self, account_holder):
        self.accounts.append(account_holder) 
        print(f"Account created")                 
        
    def find_account(self, account_number):
        for account in self.accounts:
           if account.account_number == account_number:
              print(f"account holder name : {account.account_holder}")  
              return account 
        return None
              
              
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for account in self.accounts:
                file.write(f"Account number is : {account.account_number} \n")
                for i, transaction in enumerate(self.account): 
                    print(f"Transaction index : {i} | transaction details : {transaction}")
                print(f"Post saved to {filename}")           
        

Commercial = Banking_system()
new_account = BankAccount("5302174", "Miss W.P.Nadeesha", 4000, 0)
Commercial.create_account(new_account)  
account = Commercial.find_account("5302174")
if account:
    account.view_balance()
      