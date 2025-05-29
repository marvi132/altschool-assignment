import csv

write_data = [
    ['#', 'customer_name', 'total_amount_spent']
]

# read the data
with open('results/top_customers.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    next(data, None) # skip the header of the csv file
    for row in data:
        row[1] = row[1].title()
        amount = int(row[2])
        row[2] = '₦{:,.2f}'.format(amount)
        write_data.append(row)

# Write the cleaned data
with open('results/top_customers_cleaned.csv', 'w') as f:
    csv_writer = csv.writer(f) # create a csv write object
    csv_writer.writerows(write_data)


    
        
