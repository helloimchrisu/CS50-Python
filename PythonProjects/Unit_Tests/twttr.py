def main():
    word = input("input: ")
    print(shorten(word))


def shorten(word):   
    vowel = "AEIOUaeiou"
    for char in vowel:
        word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()