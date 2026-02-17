
def LogginSuccess(func):
  def wrapper(user):
    if user == "admin":
      return func(user)
    else:
      print("Access denied")
  return wrapper

@LogginSuccess
def dashboard(user):
    print("Welcome to dashboard")

dashboard("admin")
dashboard("user")