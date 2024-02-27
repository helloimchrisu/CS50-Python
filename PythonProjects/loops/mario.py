#print("#")
#print("#")
#print("#")

#-----------------------

#for _ in range(3):
#    print("#")

#-------------------------

#def main():
#    print_column(3)
#
#
#
#
#def print_column(height):
#    for _ in range(height):
#        print("#")
#
#main()

#--------------------

#def main():
#    print_row(4)
#
#def print_row(width):
#    print("?" * width)
#main()

#--------------------

def main():
    print_square(3)


def print_square(size):


    #for each row in square
    for i in range(size):
        # print("#"*size) or 
        print_row(size)

def print_row(width):
    print("#"*width)




main()
