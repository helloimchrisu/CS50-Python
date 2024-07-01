import random

while True:
    level = int(input("Level: "))
    if level > 0:
        number = random.randint(1, level)
        while True:
            guess = int(input("Guess: "))
            if guess > number:
                print("Too large!")
            elif guess < number and guess > 0:
                print("Too small!")
            elif guess == number: 
                print("Just right!")
                break   
    break   




# print(number)