import sys

def main():
    file_name  = sys.argv[1]
    print(how_many(file_name))




def how_many(name):
    
    with open(str(name), "r") as file:
        row = 0
        for _ in file:
            row + 1
        return str(row)








def ends_with_py(name):
    if str(name).endswith(".py" ):
        return "yes"
    else:
       return "no"    




if __name__ == "__main__" :
    main()