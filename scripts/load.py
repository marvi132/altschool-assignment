import csv
input_file = '../results/top_customers_cleaned.csv'
with open(input_file, mode='r',encoding ='utf-8-sig') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        name = row['customer_name']
        amount = row['total_amount_spent']
        print(f"Loading: {name} - {amount}")
    