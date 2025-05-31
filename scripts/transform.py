# AUTHOR: Antonio Sergio Borges Goncalves Ramos Furtado
# SCRIPT: Transform.py
# DESCRIPTION: This script transform first letter of client name to upper case
# and format the total_amount and save in file

print("STARTING THE PROCESS")
file = open("../results/top_customers.csv")
cleaned_file = open("../results/top_customers_cleaned.csv", "w", encoding="utf-8")

header = file.readline()
cleaned_file.write(header)

end_of_file = False
line = ''
customer_id = 0
customer_name = ''
total_amount = ''

while not end_of_file:
    line = file.readline()

    if line != '':
        customer_id = line.split(",")[0]
        customer_name = line.split(",")[1]
        total_amount = float(line.split(",")[2])

        cleaned_file_record = f"{customer_id},{customer_name.title()}, \u20a6{total_amount:,.2f}\n"
        cleaned_file.write(cleaned_file_record)
    else:
        end_of_file = True

print("FINISHING THE PROCESS")
file.close()
cleaned_file.close()


