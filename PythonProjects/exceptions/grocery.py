try:
    i = 0
    grocery_list = {}
    while True:               
            shopping_item = input("Item: ")
            grocery_list[i] = shopping_item
            i = i+1

except EOFError:
    for item in grocery_list.values():
        print(item)