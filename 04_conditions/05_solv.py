marks = int(input("Enter marks "))

if marks >= 90 and marks <= 100:
  Grade = "A"
elif marks >= 75 and marks < 90:
  Grade = "B"
elif marks >= 60 and marks < 75:
  Grade = "C"
elif marks >=40 and marks < 59:
  Grade = "D"
else:
  Grade = "Fail"

print("Grade of Student: ",Grade)