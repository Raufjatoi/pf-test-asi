num = int(input("Enter a number: "))

if num < 0:
  print("Can't calculate factorial for negative numbers.")
else:
  factorial = 1
  for i in range(1, num + 1):
    factorial *= i
  print(f"The factorial of {num} is: {factorial}")
