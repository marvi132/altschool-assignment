import csv

# Input and output file paths
input_file = "retail-etl-assignment/results/top_customers.csv"
output_file = "retail-etl-assignment/results/top_customers_cleaned.csv"

# Function to format amount as ₦ currency
def format_currency(amount):
    return f"₦{float(amount):,.2f}"

# Read the input CSV, transform, and write to output CSV
with open(input_file, mode='r', encoding='utf-8') as infile, \
     open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.DictReader(infile)
    # Define fieldnames based on actual CSV headers
    fieldnames = ['customer_id', 'name', 'total_spent']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        # Convert full name to title case
        row['name'] = row['name'].title()
        # Format total_spent as currency
        row['total_spent'] = format_currency(row['total_spent'])
        # Write the transformed row
        writer.writerow(row)

print(f"Transformed data saved to {output_file}")

# Input file path
input_file = "retail-etl-assignment/results/top_customers_cleaned.csv"

# Read and print each row
with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        print(f"Loading: {row['name']} - {row['total_spent']}")