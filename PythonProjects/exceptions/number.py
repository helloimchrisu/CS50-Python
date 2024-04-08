def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try: 
            return int(input(prompt))
           #  x = int(input("What's x? "))
        except ValueError:
            pass
        #pass ignores input and asks for it again
            # print("x is not an integer")
        # else:
            # return x 
            #break
    # return x 
    # return breaks the loop 
main()