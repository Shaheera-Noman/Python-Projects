print("Welcone to the BMI Generator.")

weight = input("What is your weight?\n")
height = input("What is your height?\n")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = round(weight_as_int/height_as_float ** 2)
bmi_as_int = bmi

print(f"Your BMI Generator could be {bmi_as_int}")

if bmi_as_int < 18.5:
    print(f"Your BMI is {bmi_as_int}, You are underweight")
elif bmi_as_int < 25:
    print(f"Your BMI is {bmi_as_int}, You have a normal weight")
elif bmi_as_int < 30:
    print(f"Your BMI is {bmi_as_int}, You are overweight")
elif bmi_as_int < 35:
    print(f"Your BMI is {bmi_as_int}, You are obese")
else:
    print(f"Your BMI is {bmi_as_int}, You are clinically obese")
    


