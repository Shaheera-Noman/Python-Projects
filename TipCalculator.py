#If the bill was 150$, split between 5 people, with 125 tip.
#Each person should pay (150/5)*1.12 = 33.6.
#Round the result to 2 decimal places +33.60

print("Welcome to the Tip Calculator")
bill = float(input("What is your total bill? $ \n"))
tip = int(input("How much tip would you like to give? 10, 12, 15 \n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
print(f"Your Total Bill is $ {total_bill}")
bill_per_person = total_bill/people
print(f"Each person should pay $ {bill_per_person}")