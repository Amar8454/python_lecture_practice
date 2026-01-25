# key based
# it based on key value pair
# it write on curly braces { }


student = {
  "name" : "Amarjit",
  "age" : 23,
  "course" : "Python",
  "is_Active" : True
}

# print(student)

# Dictionary access

print(student["name"])
print(student.get("name"))

student["gender"] = "male"
print(student)

tea_shop = {
  "chai" : {"masala" : "testy" , "lemon" : "kadawa"},
  "tea" : {"green" : "mild" , "black" : "strong"}
}

print(tea_shop["chai"])
print (tea_shop["chai"]["masala"])

print(tea_shop["tea"].pop("green"))

# loop on dictionary data type

for key , value in student.items():
  print(key , value)

squared_num = {x : x**2 for x in range(6)}
print(squared_num)