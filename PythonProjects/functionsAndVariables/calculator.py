#nesting 
# x =  int(input("What's x? "))
# y = int(input("What's y?"))

#float for decimals  
# x = float(input("What's x? "))
#y = float(input("What's y?"))

# change string to int 
# z = int(x) + int(y)

#rounding
# z = round(x + y)

#round to 2 num after coma 
#z = round(x/y, 2)

# z = (x/y)
# print(f"{z:.2f}")

def main():
    x = int(input("What's x? "))
    print("x squared", square(x))

def square(n):
     # return n*n
     # return n**2 
      return pow (n, 2)
main()