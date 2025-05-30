import csv
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Load the CSV file using absolute path
input_path = os.path.join(project_root, 'Results', 'top_customers.csv')

# Read and transform the data
transformed_data = []
with open(input_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames or []
    
    for row in reader:
        # Convert customer names to title case
        row['customer_name'] = row['customer_name'].title()
        
        # Format amount as Nigerian Naira (₦) with comma separators and two decimal places
        total_spent = float(row['total_spent'])
        row['total_spent'] = f"₦{total_spent:,.2f}"
        
        transformed_data.append(row)

# Save the cleaned data to a new CSV file
output_path = os.path.join(project_root, 'Results', 'top_customers_cleaned.csv')
with open(output_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(transformed_data)

print(f"Cleaned data saved to: {output_path}")