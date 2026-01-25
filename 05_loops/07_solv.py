num = 9
isPrime = True

if num <= 1:
  print("NOT Prime number")
else:
  isPrime = True

  for i in range( 2, num):
    if num % i == 0:
      isPrime = False
    break

print(isPrime)

