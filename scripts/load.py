# AUTHOR: Sarah Iniobong Uko
# SCRIPT: load.py
# DESCRIPTION: This script reads the cleaned file and print each row on the screen

import csv

output_file = 'results/top_customers_cleaned.csv'

with open(output_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        print(f"Loading: {row['customer_name']} - {row['total_amount_spent']}")