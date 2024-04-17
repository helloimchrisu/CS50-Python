try:
    menu_items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    cash = 0 
    while True:
        user_item = input("Item: ")
        for item in menu_items:
            cash = cash + menu_items[user_item]
            break
except EOFError:
    print(cash)
