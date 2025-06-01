import csv

# Load the input CSV
input_file_path = r'C:\Users\USER\Desktop\codebook\alt_class\retail-etl-assignment\results\top_customers.csv'
output_file_path = r'C:\Users\USER\Desktop\codebook\alt_class\retail-etl-assignment\results\top_customers_cleaned.csv'

# Read the input CSV file
with open(input_file_path, mode='r', newline='', encoding='utf-8') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    rows = []
    for row in csvreader:
        name = row[0].title()  # Convert name to title case
        amount = float(row[1])  # Convert amount to float
        formatted_amount = f"₦{amount:,.2f}"  # Format to Naira with comma and 2 decimal places
        rows.append([name, formatted_amount])

# Write the cleaned data to a new CSV file
with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)  # Write header
    csvwriter.writerows(rows)   # Write cleaned rows


# File path to the cleaned CSV
file_path = r'C:\Users\USER\Desktop\codebook\alt_class\retail-etl-assignment\results\top_customers_cleaned.csv'

# Open and read the cleaned CSV file
with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csvreader = csv.reader(file)
    
    # Skip the header row
    header = next(csvreader)

    # Print each customer's record in the required format
    for row in csvreader:
        name = row[0]
        amount = row[1]
        print(f"Loading: {name} - {amount}")

