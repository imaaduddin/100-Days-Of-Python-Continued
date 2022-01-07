################### Scope ####################
# No such thing as block scope on Python

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") #local scope, meaning 2 for enemies can be accessed only insside this function 

increase_enemies()
print(f"enemies outside function: {enemies}") 
# Above this a global scope as 1 is not inside a function and can be accessed anywhere 


# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) # this variable is not global meaning you cannot access it unless in the function 


# Global Scope 
player_health = 10

def player_stats():
    attack = 85
    print(attack)
    print(player_health)

print(player_health)
# Over here player_health variable can be accessed outside and inside the function as it is a global variable 



# There is no Block Scope
game_level = 3
enemies = ["aliens", "zombies", "skeletons"]

def create_enemy():  
  if game_level < 5:
        new_enemy = enemies[0]

  print(new_enemy)
