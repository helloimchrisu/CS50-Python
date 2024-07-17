def main():
    while True:
        try:
            user_fraction = input("Fraction: ")
            fraction = convert(user_fraction)
            print(gauge(fraction))
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass



def convert(fraction):
    x,y = fraction.split("/")
    percentage = (int(x) / int(y)) * 100
    rounded_fraction = round(percentage)
    return rounded_fraction

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()