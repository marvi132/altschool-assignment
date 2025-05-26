import csv
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Load the cleaned CSV file using absolute path
input_path = os.path.join(project_root, 'Results', 'top_customers_cleaned.csv')

# Read and print each row
with open(input_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        customer_name = row['customer_name']
        total_spent = row['total_spent']
        print(f"Loading: {customer_name} - {total_spent}")