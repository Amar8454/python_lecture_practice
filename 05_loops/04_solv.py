input_num = int(input("Enter number: "))

original = input_num
isPalindrome = True
reverse = 0

while input_num !=0:
  digit = input_num % 10
  reverse = reverse * 10 + digit
  input_num = input_num // 10

if (reverse == original):
  isPalindrome = True
else: 
  isPalindrome = False

print(isPalindrome)




