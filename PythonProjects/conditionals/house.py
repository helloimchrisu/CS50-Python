name = input("Whats your name? ")

#if name == "Harry" or name == "Hermione" or name == "Ron":



#    print("Gryffindor")
#elif name == "Hermione":
#    print("Gryffindor")
#elif name == "Ron":
#    print("Gryffindor")


#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
#    case "Hermione":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")