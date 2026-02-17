

class Bank:
  def __init__(self , bank_name , ifsc_code , branch):
   self.bank_name = bank_name
   self.ifsc_code = ifsc_code
   self.branch = branch
   self.accounts = {}
   
  def add_account(self , account):
    self.accounts[account.account_no] = account
  
  def show_bank_info(self):
    print(f"Bank Details : bank name: {self.bank_name} , IFSC_Code: {self.ifsc_code} , branch: {self.branch} ")

class User:
  def __init__(self , name , age , phone , email , address ):
    self.name = name
    self.phone = phone
    self.age = age
    self.email = email
    self.address = address
    
  def show_user_info(self):
    print(f"user inoformations : {self.name} ,{self.age} , {self.phone} ,{self.address} ")


class Account:
  def __init__(self , account_no , user , account_type):
    self.account_no = account_no
    self.user = user
    self.balance = 0
    self.account_type = account_type

  def deposite(self , amount):
    self.balance += amount
    print(f"Your deposite money : {amount}")

  def withdraw(self , amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"Your withdraw money : {amount} ")
    else:
      print("Insufficient balance")
  
  def checkBalance(self):
    print(f"Your Available Balance: {self.balance}")


bank = Bank("State Bank of India" , "SBI0012345" , "Majhaulia")
bank.show_bank_info()

user1 = User("Amarjit" , 23 , 9123228139 , "amarjit@gmail.com" , "majhaulia")
user1.show_user_info()

acccount = Account(123456356 , user1 , "saving")
bank.add_account(acccount)

acccount.deposite(4500)
acccount.withdraw(2000)
acccount.checkBalance()
