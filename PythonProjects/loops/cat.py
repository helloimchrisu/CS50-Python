# print("meow")
# print("meow")
# print("meow")

# i = 3 
# while i != 0:
#     print("meow")
#     i = i - 1

# i = 0 
# while i < 3:
#     print("meow")
#     i += 1    

# for i in [0, 1, 2]:
#     print("meow")

# if you dont use variable name it _
 # for _ in range(3):
#     print("meow")

# print("meow\n" * 3, end="")

# whlie True: - infinite loop
#while True:
#    n = int((input("What's n? ")))
#    if n > 0:
#        break
#
#for _ in range(n):
#    print("meow")

def main():
    meow(3)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n    

def meow(n):
    for _ in range(n):
        print("meow")