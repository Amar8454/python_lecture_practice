# based on index
# written in brackets
# muttable

tea_list = ["Lemon" , "Harbel" , "Ginger" , "Masala"]

# access tea_list
print(tea_list[0])
print(tea_list[-1])

#add tea in tea_list last index
tea_list.append("Black")
tea_list.insert(3,"White")
print(tea_list)

# part nikalana
print(tea_list[1:3])
print(tea_list[0:4:2])

# loop on tea_list
for tea in tea_list:
  print(tea)