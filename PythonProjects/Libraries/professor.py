import random


def main():
    difficulty = get_level()
    while True:
        x,y = generate_integer(difficulty)
        answ = x + y
        user_answ = int(input(f"{x} + {y} = "))
        if user_answ == answ: 
            print("yes!")
        else:
            print("no!")


def get_level():
    level = int(input("Level: "))
    return level 


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x  = random.randint(10, 99)
        y  = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x,y 
   


if __name__ == "__main__":
    main()