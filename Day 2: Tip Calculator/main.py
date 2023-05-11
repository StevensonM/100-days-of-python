# This is a calculator that tells you how much each person has to pay, including the tip.
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percent would you like to tip? 10, 12, or 15?"))
split = int(input("How many people are splitting the bill?"))
total = float(percentage * bill)
tip_total = percentage/100
total = (tip_total + bill) / split
final_total = f"Your total is {total} per person!"
print(final_total)
