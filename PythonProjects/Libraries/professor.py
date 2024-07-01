import random
while True:
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    answ = num1 + num2
    user_answ = int(input(f"{num1} + {num2} = "))
    if user_answ != answ:
        print("EEE")

# copy to the proper structure