
def even_generater(limit):
  for i in range(2, limit+1 , 2):
    yield i
  
for num in even_generater(10):
  print(num)