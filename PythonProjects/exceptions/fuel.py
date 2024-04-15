user_fraction = input("Fraction:")
x, y = user_fraction.split("/")
fraction = (int(x)/int(y)) * 100
rounded_fraction = round(fraction)
print(f"{rounded_fraction}%")