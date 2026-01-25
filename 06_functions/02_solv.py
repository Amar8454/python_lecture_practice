number = int(input("Enter number : "))
def countNumber(number):
  count = 0
  while number != 0:
    Ldigit = number % 10
    count += 1
    number //= 10
  
  return count

result = countNumber(number)
print(result)