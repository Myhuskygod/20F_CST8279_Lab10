import csv

f = input("Please enter which file you want to read: ")
with open(f, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        print(' '.join(row))