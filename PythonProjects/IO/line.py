import sys

def main():
    file_name  = sys.argv[1]
    print(how_many(file_name))




def how_many(name):
    with open(str(name), "r") as file:
        lines = file.readlines() 
        line_count = len(lines) 
        for line in file:
            if line.startswith("#"):
                line_count - 1
            return line_count








def ends_with_py(name):
    if str(name).endswith(".py" ):
        return "yes"
    else:
       return "no"    




if __name__ == "__main__" :
    main()