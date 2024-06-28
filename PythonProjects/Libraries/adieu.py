import inflect
p = inflect.engine()
try:
    names = []
    while True:
        name = input("Name: ")
        names.append(name)
    


except EOFError:
        print("Adieu, Adieu " + p.join(names))
    