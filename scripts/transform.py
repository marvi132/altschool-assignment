import csv

# Input and output file paths
input_file ='results/top_customers.csv'
output_file = "results/top_customers_cleaned.csv"

#Formating amount as ₦ currency
def format_currency(amount):
    return f"₦{float(amount):,.2f}"

# Read the input CSV, transform, and output CSV
with open('results/top_customers.csv', 'r', encoding='utf-8') as infile, \
     open('results/top_customers_cleaned.csv', 'w', encoding='utf-8', newline='') as outfile:

    reader = csv.DictReader(infile)
    # Define fieldnames based on actual CSV headers
    fieldnames = ['id', 'name', 'total_amount_spent']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Convert full name to title case
        row['name'] = row['name'].title()
        # Format total_spent as currency
        row['total_amount_spent'] = format_currency(row['total_amount_spent'])
        # Write the transformed row
        writer.writerow(row)

print(f"Transformed data saved to {output_file}")

# Input file path
input_file = "results/top_customers_cleaned.csv"

# Read and print each row
with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        print(f"Loading: {row['name']} - {row['total_amount_spent']}")