
def outer(num):
  num += 5
  print("sum of num in outer fun  : " , num)
  
  def inner():
    print ("sum of number in inner fun  : ", num)

  inner()
 # return inner

# fn = outer(5)
# fn()

outer(5)