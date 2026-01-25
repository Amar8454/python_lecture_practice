balance = int(input("Enter your balance: "))
withdrawal = int(input("Enter your withdrawal money: "))

def withdrawalMoney(balance , withdrawal):
  if withdrawal <= balance:
    print("withdrawal is success")
  else:
    print("balance is not Enough")

withdrawalMoney(balance , withdrawal)