import random

secret_num = random.randint(1, 100)
guesses = 5

for attempt in range(guesses):
  guess = int(input(f"Guess the number between 1 and 100 (you have {guesses - attempt} attempts left): "))

  if guess == secret_num:
    print(f"Congratulations! You guessed the number in {attempt + 1} attempts!")
    break
  elif guess < secret_num:
    print("Your guess is too low, try higher!")
  else:
    print("Your guess is too high, try lower!")

  if attempt == guesses - 1:
    print(f"Sorry, you ran out of guesses. The number was {secret_num}.")

