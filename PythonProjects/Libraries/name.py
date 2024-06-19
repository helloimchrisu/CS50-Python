# printing input from terminal
import sys   

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments") # exit program

# Print name tags 
print("hello, my name is", sys.argv[1])
