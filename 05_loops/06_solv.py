nums = [3, 7, 2, 9, 4, 1]
max = 0
min = 0
for num in nums:
  if max < num:
    max = num
  else:
    min = num

print(min)
print(max)