def main():
    userTime = input("What's the time? ")
    # hours, minutes = time.split(":")
    # hours = convert(hours)
    # minutes = convert(minutes)
    userTime = convert(userTime)


    def convert(time):
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)




main()