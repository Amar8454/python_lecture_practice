num_input = int(input("Enter input number: "))

reverse = 0
while num_input != 0:
  digit = num_input % 10
  reverse = reverse * 10 + digit
  num_input = num_input // 10

print(reverse)