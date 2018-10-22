import random

Player_health = 50
difficulty = 3
health_potion = random.randint(25,50)
updated_potion = health_potion-(random.randint(5,10)*difficulty)
print(updated_potion)
Player_health = Player_health + updated_potion
print(Player_health)
