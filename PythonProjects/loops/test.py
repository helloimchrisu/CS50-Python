plate = input()
array_lenght = len(plate) - 1
for s in plate:
    if s.isnumeric() == True and plate[array_lenght].isalpha() == True:
        print("true")
    else:
        print("false")
   