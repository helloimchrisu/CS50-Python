def main():
   userInput1 = input("What would you like to say?")
   convert(userInput1)
def convert(userInput): 
    userInput = userInput.replace(":)", "🙂")
    userInput = userInput.replace(":(", "🙁")
    print(userInput)

      

main()