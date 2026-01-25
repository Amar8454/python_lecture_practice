years = int(input("Enter years.. "))

if years % 400 == 0 or (years % 4 == 0 and years % 100 != 0):
  print("Leap Years")
else:
  print("NOT Leap Years")