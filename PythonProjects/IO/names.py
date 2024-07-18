# names = []
#
#for _ in range(3):
#    # name = input("What's your name? ")
#    names.append(input("What's your name? "))
#
#for name in sorted(names):
#    print(f"hello, {name}")

#--------------------------------------------------------
#creating file that stores the names
#name = input("What's your name? ")
#
#better way to open and close a file 
#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")
#file.close()
#-----------------------------------------------
#best way to print text
#with open("names.txt", "r") as file:
#    for line in file:
#        print("hello,", line.rstrip())

#old way
#    lines = file.readlines()
#
#for line in lines:
#   print("hello", line.rstrip())
#--------------------------------------------

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")