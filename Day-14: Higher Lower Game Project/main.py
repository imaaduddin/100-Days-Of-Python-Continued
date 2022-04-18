from socket import AF_LLC
from game_data import data
from art import logo 
from art import vs
import random

def get_random_account():
    # Get data from random account
    return random.choice(data)

def format_data(account):
    # Format account into printable text: name, description and country
    name = account['name']
    description = account['description']
    country = account['country']
    
    return f'{name}, a {description}, from {country}'

def check_answer(guess, a_followers, b_followers):
    # Checks followers against user's guess and returns True if they got it right
    # Or false if they got it wrong
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
        
    
def game():
    print(logo)
    score = 0
    game_should_continue = True 
    account_a = get_random_account()
    account_b = get_random_account()