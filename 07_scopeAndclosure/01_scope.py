
number = 10        # global variable (it access anywhere)
# print(number)


def my_fun():
  number = 20    # local variable   (it access only inside current function)
  print(number)   

my_fun()
print(number) # it access local variable


def outer(num):
  num = num * 2          # here parent num variable access child 
  def inner():
    print(num)
  inner()

outer(5)           # 10


# it show error beacuse it not closure function here not pass a parameter in inner functions
# it inner functions only use outer variable

def outer():
  num = num + 2
  print(num)                                                  
  def inner(num):
    pass 
  return inner(5)

outer()