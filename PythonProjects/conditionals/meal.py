def main():
    userTime = input("What's the time? ")
    userTime = convert(userTime)

    if 7.00 <= userTime <=8:
        print("breakfast time!")
    elif 12 <= userTime <= 13:
        print("lunch time!")
    elif 18 <= userTime <= 19:
        print("dinner time!")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)    
    return (hours + (minutes/60)) 
        

main()