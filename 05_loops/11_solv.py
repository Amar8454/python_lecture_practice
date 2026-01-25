
# Armstrong number

num = 153
temp = num
Ldigit = len(str(num))
sum_of_power = 0

while temp > 0:
  digit = temp % 10
  sum_of_power += digit ** Ldigit
  temp //= 10

if num == sum_of_power:
  print ("armstrong")
else:
  print ("not armstrong")
  
