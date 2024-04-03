

fruits = [
    {"name" : "apple", "kcal" : "130"},
    {"name" : "avocado", "kcal" : "50"},
    {"name" : "banana", "kcal" : "130"},
    {"name" : "cantaloupe", "kcal" : "50"},
    {"name" : "grapefruit", "kcal" : "60"},
    {"name" : "grapes", "kcal" : "90"},
    {"name" : "honeydew melon", "kcal" : "50"},
    {"name" : "kiwifruit", "kcal" : "90"},
    {"name" : "lemon", "kcal" : "15"},
    {"name" : "lime", "kcal" : "20"},
    {"name" : "nectarine", "kcal" : "60"}
]



user_fruit = input("Item: ")
for fruit in fruits:
        if user_fruit in fruit["name"]:
            print(fruit["kcal"])
            break