import csv

home = input("What is your house? ")
name = input("What is your name? ")

with open("student.csv", mode = 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
