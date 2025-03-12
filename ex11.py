print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
BMI = float(weight)/(float(height)/100)**2

if BMI < 18.4:
	status = "Underweight"
elif BMI < 24.9:
	status = "Normal"
else:
	status = "Fatass"

print(f"So, you are {age} old, {height} centimeters tall and weigh {weight} kilograms. Your BMI is {BMI} and you are {status}")