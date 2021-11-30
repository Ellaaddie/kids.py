import random
Dice1 = (1,6)
Dice2 = (1,6)
name = ["Tolani", "Steve"]
User = random.choice(name)
roll = random.choice(Dice1)
roll2 = random.choice(Dice2)
Question = input("Are you ready to play? (y/n)")
if Question == "y":
    print(User)
if roll and roll2 == 6:
    print("Game on")
