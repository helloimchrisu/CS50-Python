def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(ex_plate):
    if 2> len(ex_plate) or len(ex_plate) > 6:
        return False
    elif ex_plate.isalnum() == False:
        return False
    elif ex_plate[0:1].isalpha() == False:
        return False
    elif  letters_in_mid(ex_plate) == False:
        return False
    else:
        return True

def letters_in_mid(plate):
    array_lenght = len(plate) - 1
    plate_list = list(plate)
    for s in plate_list:
        if s[0:array_lenght-1].isnumeric() == True and plate[array_lenght].isalpha() == True:
            return False
            


    
        
        
main()