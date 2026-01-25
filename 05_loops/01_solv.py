
sum = 0
for num in range(1, 101):
  if num % 2 == 0:
    sum += num
 
print("total sum of even nums: " ,sum)

sumOdd = 0
for num in range (1, 101):
  if num % 2 != 0:
    sumOdd +=num
print("total sum of odd nums: ", sumOdd)