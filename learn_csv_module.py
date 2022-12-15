import csv

with open('example.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        print(','.join(row))