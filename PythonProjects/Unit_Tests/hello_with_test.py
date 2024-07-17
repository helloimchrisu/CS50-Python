def main():
    name = input("Hello")
    print(hello(name))

def hello (to="world"):
    #print("hello,", to )
    #it's better to return value than print
    return f"hello, {to}"

if __name__ == "__main__":
    main()