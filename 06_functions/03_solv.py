year = int(input("Enter year : "))

def leap_year(year):
  if ( year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) ) :
    print ("Leap year ")
  else:
    print("NOT Leap year ")

leap_year(year)