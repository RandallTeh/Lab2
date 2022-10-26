def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))

 BMI = weight / (height * height)

 if BMI < 18.5:
  print("underweight")
 elif BMI >= 18.5 and BMI <= 25:
  print("normalweight")
 else:
  print("overweight")


 print(BMI)

calculate_bmi(weight=57, height=1.73)