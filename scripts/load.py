# AUTHOR: Antonio Sergio Borges Goncalves Ramos Furtado
# SCRIPT: load.py
# DESCRIPTION: This script reads the cleaned file and print each row on the screen

file = open("../results/top_customers_cleaned.csv", encoding="utf-8")

end_of_file = False
line = ''
customer_id = 0
customer_name = ''
total_amount = ''

while not end_of_file:
    line = file.readline()

    if line != '':
        customer_name = line.split(",", 2)[1]
        total_amount = line.split(",", 2)[2]
        print(f"Loading: {customer_name} - {total_amount}")
    else:
        end_of_file = True
