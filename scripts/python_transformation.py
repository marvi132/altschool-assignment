import csv, os 


input_file = 'C:/Users/Fatai Badmus/OneDrive/Desktop/retail-data-engineeringsqltask_1_queries/Query_1_top_customers.csv'
output_file = 'C:/Users/Fatai Badmus/OneDrive/Desktop/retail-data-engineeringsqltask_1_queries/Query_top_customers_final.csv'


with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile) 
    
    fieldnames = ['customer_name', 'total_spent']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        name = row['customer_name'].title()
        amount = float(row['total_spent'])
        formatted_amount = f"₦{amount:,.2f}"
        
        writer.writerow({
            'customer_name': name,
            'total_spent': formatted_amount
        })

print("Output saved to Query_top_customers_final.csv")

os.startfile(output_file)
