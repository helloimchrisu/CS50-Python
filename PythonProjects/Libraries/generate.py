# generating random coin toss

# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)
#-----------------------------------------
# generating random number

# import random  

# number = random.randint(1,10)
# print(number)
#------------------------------------------
# shuffling cards
import random 

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)