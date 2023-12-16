number_of_people = int(input("Enter number of people: "))
cost_of_meal = int(input("Enter the cost of each meal: "))
sales_tax_rate = 20.00 / 100  # Convert percentage to decimal
tip_rate = 5.00 / 100  # Convert percentage to decimal

meal_cost_per_person = cost_of_meal
total_cost_per_person = meal_cost_per_person * (1 + sales_tax_rate + tip_rate)

# Alternatively, you can combine everything in one line:
# total_cost_per_person = cost_of_meal * (1 + sales_tax_rate + tip_rate)

total_bill_amount = total_cost_per_person * number_of_people

print(f"Total cost per person (including tax and tip): ${total_cost_per_person:.2f}")
print(f"Total bill amount: ${total_bill_amount:.2f}")
