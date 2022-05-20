from socket import AF_LLC
from game_data import data
from art import logo 
from art import vs
import random

# Display art
print(logo)

# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

# Format the account data into printable format
account_name = account_a['name']
account_description = account_a['description']
account_country = account_a['country']
print(f'{account_name}, a {account_description}, from {account_country}')


