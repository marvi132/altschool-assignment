import csv

with open('results/top_customers_cleaned.csv', 'r') as file:
    data = csv.reader(file)
    next(data, None) # skip the headerfile

    for row in data:
        print(f'Loading: {row[1]} - {row[2]}')