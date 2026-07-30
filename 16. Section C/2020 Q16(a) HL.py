# Q16 (a) 2020
# Name = Ms.Meade

#(v)
#def display_intro():
#    print("Welcome to the BMI Calcaultor!")

#display_intro()

print("Welcome to the BMI Calcaultor!")
weight = int(input("Enter your weight (in kilograms): ")) #read weight
height = int(input("Enter your height (in centimeters)")) #centimeters
bmi= round((weight/ (height**2)* 10000),1)


print("BMI is: ", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <=24.9:
    print("Normal")
elif bmi>=25 and bmi<=29.9:
    print("Overweight")
else:
    print("Obese")


