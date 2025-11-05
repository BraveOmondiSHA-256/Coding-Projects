print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_percentage = bill * float(tip) / 100
total_bill = bill + bill_percentage
bill_per_person = total_bill / people
print(f"Each person should pay:{round(bill_per_person, 2)}")