

def my_fun(**kwargs):
  print(kwargs)
  for key , value in kwargs.items():
    print(f"{key}: {value}")

my_fun(name= "Amarjit" , age=23)
my_fun(name="shaktiman" , power="lazer", role= "actor")