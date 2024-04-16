while True:
    try:
            user_fraction = input("Fraction:")
            x, y = user_fraction.split("/")
            fraction = (int(x)/int(y)) * 100
            rounded_fraction = round(fraction)        
            if fraction >= 99:
                print("F")
            elif fraction <= 1:
                print("E")
            else:
                print(f"{rounded_fraction}%")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
         pass
