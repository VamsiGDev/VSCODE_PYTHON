# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇  
x = round(weight / height**2)

if x < 18.5:
    print(f"Your BMI is {x}, you are underweigth.")
elif x < 25:
    print(f"Your BMI is {x}, you have a normal weight.")
elif x < 30:
    print(f"Your BMI is {x}, you are slightly overweight.")
elif x < 35:
    print(f"Your BMI is {x}, you are obese.") 
else:
    print(f"Your BMI is {x}, you are clincally obese.") 