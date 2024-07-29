#import csv

#name = input("What's your name? ")
#home = input("What's your home? ")
#
#with open("students1.csv", "a") as file:ss
#    writer = csv.writer(file)
#    writer.writerow([name, home])

import csv 

name = input("What's your name? ")
home = input("What's your home? ")

with open("students1.csv", "a") as file:
    writer = csv.DictWriter(file,fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})