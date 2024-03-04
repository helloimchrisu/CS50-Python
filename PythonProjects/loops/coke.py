coke = 50
while True:
    print("Amount due: " + str(coke))
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25: 
        coke = coke - coin
        if coke <= 0:
            coke = coke*-1
            print("Change owed: " + str(coke))
            break

        
   


