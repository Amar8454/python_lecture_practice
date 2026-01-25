password = input("Enter password: ")
password_length = len(password)

if password_length >= 8:
  print("Valid password")
else:
  print("Invalid password")