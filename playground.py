import csv
with open('beatles-diskography.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Title'], row['Released'])
