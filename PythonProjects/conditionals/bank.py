def main():
    greeting = input("Greeting: ").replace(" ", "")
    firstChar = greeting[0]
    
    #print("20$")
    if greeting.startswith("Hello") == True:
        print("0$")
    elif firstChar == "H": 
        print("20$")
    else:
        print("100$")

main()
