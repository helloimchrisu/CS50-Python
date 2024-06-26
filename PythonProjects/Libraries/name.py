# printing input from terminal
import sys   

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments") # exit program
# elif len(sys.argv) > 2:
#    sys.exit("Too many arguments") 

# Print name tags 

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
