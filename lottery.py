# Problem 3:

# Develop a program to play a lottery. The program randomly generates a two-digit number, prompts the
# user to enter a two-digit number, and determines whether the user wins according to the following rules:

# • If the user’s input matches the lottery in the exact order, the award is Rs 10,000.
# • If all the digits in the user’s input match all the digits in the lottery number, the award is Rs 3,000.
# • If one digit in the user’s input matches a digit in the lottery number, the award is Rs1,000


import random

# Generate a random two-digit lottery number
lottery = random.randint(10, 99)

# Ask the user to input a two-digit number
user_input = int(input("Enter a two-digit number: "))

# Extract digits from the lottery number
lottery_tens = lottery // 10
lottery_ones = lottery % 10

# Extract digits from the user's input
user_tens = user_input // 10
user_ones = user_input % 10

# Check if the user wins according to the rules
if user_input == lottery:
    print(f"Congratulations! You win Rs 10,000. The lottery number was {lottery}.")
elif user_tens == lottery_tens and user_ones == lottery_ones:
    print(f"Congratulations! You win Rs 3,000. The lottery number was {lottery}.")
elif user_tens == lottery_ones or user_ones == lottery_tens:
    print(f"Congratulations! You win Rs 1,000. The lottery number was {lottery}.")
else:
    print(f"Sorry, you didn't win. The lottery number was {lottery}.")
