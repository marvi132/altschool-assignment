import csv
file_path = '/Users/home/Documents/Altschool_project/retail-etl-assignment/results/top_customers_cleaned.csv'

with open(file_path, mode='r',newline='', encoding='utf-8') as file:
    #Create a DictReader to parse rows as dictionaries using the header
    reader = csv.DictReader(file)

    for row in reader:
        # Print each customer's name and total amount spent
        print(f'Loading: {row["name"]} - {row["total_spent"]}')
