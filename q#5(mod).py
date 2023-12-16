number_of_people = int(input("Enter number of people: "))
cost_of_meal = int(input("Enter the cost of each meal: "))
sales_tax_rate = 20.00 / 100  # Convert percentage to decimal
tip_rate = 5.00 / 100  # Convert percentage to decimal

meal_cost_per_person = cost_of_meal
# Calculate total cost including tax and tip
total_cost_per_person = meal_cost_per_person * (1 + sales_tax_rate + tip_rate)

# Calculate total bill amount
total_bill_amount = total_cost_per_person * number_of_people

# Calculate sales tax and tip amounts
sales_tax_per_person = meal_cost_per_person * sales_tax_rate
tip_per_person = meal_cost_per_person * tip_rate

# Print all desired information
print(f"Total cost per person (including tax and tip): ${total_cost_per_person:.2f}")
print(f"Cost of each person: ${meal_cost_per_person:.2f}")
print(f"Total sales tax: ${sales_tax_per_person * number_of_people:.2f}")
print(f"Total tip: ${tip_per_person * number_of_people:.2f}")
print(f"Sales tax percentage applied: {sales_tax_rate * 100:.2f}%")
print(f"Tip percentage applied: {tip_rate * 100:.2f}%")
print(f"Total bill amount: ${total_bill_amount:.2f}")

