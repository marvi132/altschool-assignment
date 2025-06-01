import csv
input_file = 'results/top_customers.csv'
output_file = 'results/top_customers_cleaned.csv'

# Reading the CSV and transform the data
with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)
    fieldnames = ['customer_id', 'customer_name', 'total_spent']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        # Converting customer_name to title case
        row['customer_name'] = row['customer_name'].title()
        
        # Formating total_spent to ₦ currency format
        amount = float(row['total_spent'])
        row['total_spent'] = f"₦{amount:,.2f}"
        writer.writerow(row)