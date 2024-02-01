# ask user for their name 
# name = input("Whats your name? ").strip().title()
# name2 = input("Whats second name? ")
# say hello to user 
# print("hello, " + name) 
# print("hello,", name,name2 ) 
# print("hello, ", end="")
# print(name)

# remove whitespace from str 
# name = name.strip()

#split user's name into first and last name 
# first, last = name.split()

# capitalize 1st letter of str
# name = name.capitalize()

# capitalize every 1st letter 
# name = name.title()

# name = name.strip().title()

#print(f"hello, {name}")

#define function (default hello world)

def main():

    name = input("What's your name? ")
    hello(name)

#name = to 
def hello(to="world"):
    print("hello,", to)

main() 
   
