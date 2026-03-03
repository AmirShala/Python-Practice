"""
Tip Calculator Program
----------------------

Description:
This program calculates how much each person should pay when splitting a bill,
including a selected tip percentage.

Workflow:
1. Prompts the user to enter:
   - Total bill amount
   - Desired tip percentage
   - Number of people splitting the bill
2. Calculates the total bill including tip.
3. Divides the total amount evenly between the specified number of people.
4. Displays the amount each person should pay, formatted to two decimal places.

Formula:
    amount_per_person = (bill * (1 + tip/100)) / people

Output:
The final result is displayed in currency format with exactly two decimal places.

Example:
If the bill is $100, tip is 10%, and 2 people are splitting:
Each person should pay: $55.00
"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

amount_per_person = (bill * (tip/100 + 1)) / people
print(f"Each person should pay: ${amount_per_person:.2f}")
