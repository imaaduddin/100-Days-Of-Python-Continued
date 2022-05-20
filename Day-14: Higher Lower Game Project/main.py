from game_data import data
from art import logo, vs
import random

# Format the account data into printable format
def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_description}, from {account_country}'

# Display art
print(logo)

# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f'Compare A: {format_data(account_a)}.')
print(vs)
print(f'Against B: {format_data(account_b)}.')

# Ask user for a guess 
guess = input('Who has more followers? Type "A" or "B": ').lower()

# Check if user is correct
# Get follower count of each account 
a_follower_count = account_a['follower_count']
b_follower_count = account_b['follower_count']
# Use if statement to check if user is correct 
