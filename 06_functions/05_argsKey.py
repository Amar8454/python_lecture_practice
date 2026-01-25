
def my_fun(*args):
  # print(args)
  for i in args:
      print(i * 2)
  return sum(args)

# my_fun(1 ,2 ,3,4)
result = (my_fun(1,2,3,4))
print(result)
# my_fun("amarjit" , "chirag" , "nitesh" , "golu")