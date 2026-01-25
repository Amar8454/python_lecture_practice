number = int(input("Enter your number "))

if number > 0:
  numberCheck = "positive"
elif number < 0:
  numberCheck = "negative"
else :
  numberCheck = "zero"

print(numberCheck)