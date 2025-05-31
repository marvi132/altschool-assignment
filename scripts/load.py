import csv
file_path = 'results/top_customers.csv'

with open(file_path, mode='r',newline='', encoding='utf-8') as file:
    #A DictReader to read rows as dict
    reader = csv.DictReader(file)

    for row in reader:
        # Print customer's name and total amount spent
        print(f'Loading: {row["name"]} - {row["total_amount_spent"]}')