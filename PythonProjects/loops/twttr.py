
def find_vowel(user_str):
    vowel = "AEIOUaeiou"
    for char in vowel:
        user_str = user_str.replace(char, "")
    return user_str
        

user_str = input("Input: ")
user_str = find_vowel(user_str)
print(user_str)




