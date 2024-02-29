
        


camel_case = input("camel case: ")    
for character in camel_case:
    if character.isupper() == True:
        print("_", end="")
        character = character.lower()
    print("snake case: " + character, end="")
    
            

