#Number Guessing Game Objectives:

# Include an ASCII art logo.
# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Number%20Guessing%20Game!!
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print("Pssst, the correct answer is 17")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Easy Choice
if difficulty == "easy":
    answer = random.randint(1, 100)
    print(answer)
    print("You have 10 attempts remaining to guess the number")
    guess_one = int(input("Make a guess: "))
    for i in range(10, 1, -1):
        if guess_one < answer:
            print("Too low.")
            print("Guess again.")
            print(f"You have {i - 1} attempts remaining to guess the number.")
            guess_one = int(input("Make a guess: "))
        elif guess_one > answer:
            print("Too high.")
            print("Guess again.")
            print(f"You have {i - 1} attempts remaining to guess the number.")
            guess_one = int(input("Make a guess: "))
        elif guess_one == answer:
            print(f"You got it! The answer was {answer}")
            break
        elif i == 0:
            print("You've run out of guesses, you lose.")

# Hard Choice
if difficulty == "hard":
    answer = random.randint(1, 100)
    print(answer)
    print("You have 5 attempts remaining to guess the number")
    guess_two = int(input("Make a guess: "))
    for i in range(5, 1, -1):
        if guess_two < answer:
            print("Too low.")
            print("Guess again.")
            print(f"You have {i - 1} attempts remaining to guess the number.")
            guess_two = int(input("Make a guess: "))
        elif guess_two > answer:
            print("Too high.")
            print("Guess again.")
            print(f"You have {i - 1} attempts remaining to guess the number.")
            guess_two = int(input("Make a guess: "))
        elif guess_two == answer:
            print(f"You got it! The answer was {answer}")
            break
        elif i == 0:
            print("You've run out of guesses, you lose.")
            
            
            


          