print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split bill? "))

tip_percent = tip / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount

result = total_bill / split

format(result, '.2f')

print(f"Each person should pay:  {result}")