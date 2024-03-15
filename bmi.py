height = float(input("Your height in m?\n"))

weight = float(input("Your weight in kg?\n"))

bmi = weight / height ** 2

if bmi < 18.5:
    print(f"You are underweight. BMI: {round(bmi, 2)}")
elif bmi < 25:
    print(f"You are in peak form. BMI: {round(bmi, 2)}")
elif bmi < 30:
    print(f"You are overweight. BMI: {round(bmi, 2)}")
else:
    print(f"You are obese brother. Get help. BMI: {round(bmi, 2)}")

# print(f"Weight: {weight}, Height: {height}")
# print(f"bmi: {bmi}")
