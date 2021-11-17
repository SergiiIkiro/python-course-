import csv

with open('users.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for name, email, grade in reader:
        print(f'Name: {name}\n | Email:{email}\n | Grade: {grade}\n ')
