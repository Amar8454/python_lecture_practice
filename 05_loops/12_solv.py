# product of digit number


num = 1234
product = 1
while num > 0:
  Ldigit = num % 10
  product *= Ldigit
  num //= 10

print(product)