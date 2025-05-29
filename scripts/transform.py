import csv


# Path to your CSV file
input_csv_file_path = '/Users/home/Documents/Altschool_project/retail-etl-assignment/results/top_customers.csv'
output_csv_file_path = '/Users/home/Documents/Altschool_project/retail-etl-assignment/results/top_customers_cleaned.csv'

# Open and read the CSV file
with open(input_csv_file_path, mode='r', newline='', encoding='utf-8') as inputfile, \
     open(output_csv_file_path, mode ='w', newline='', encoding='utf-8') as outputfile:
        reader = csv.DictReader(inputfile)
        field_names = reader.fieldnames

        writer = csv.DictWriter(outputfile, fieldnames=field_names)
        writer.writeheader()


        for row in reader:
            #Convert customer names to title
            row['name'] = row['name'].title()

            #Format amount into ₦ currency
            row['total_spent'] = f'₦{float(row["total_spent"]):,.2f}'

            writer.writerow(row)
            print(row)

       