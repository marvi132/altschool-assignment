import csv

input_file = 'C:/Users/Fatai Badmus/OneDrive/Desktop/retail-data-engineeringsqltask_1_queries/Query_top_customers_final.csv'


with open(input_file, 'r',  encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        print(f"Loading: {row['customer_name']} - {row['total_spent']}")