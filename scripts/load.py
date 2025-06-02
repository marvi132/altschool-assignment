import csv

def load_and_print_customers(filepath):
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader)

            try:
                customer_name_idx = header.index('customer_name')
                total_spent_idx = header.index('total_spent')
            except ValueError as e:
                print(f"Error: Missing expected column in CSV header: {e}")
                print(f"Header found: {header}")
                return

            print(f"--- Loading data from '{filepath}' ---")
            for row in reader:
                if len(row) > max(customer_name_idx, total_spent_idx):
                    customer_name = row[customer_name_idx]
                    amount_spent = row[total_spent_idx]
                    print(f"Loading: {customer_name} - {amount_spent}")
                else:
                    print(f"Warning: Unable to read row: {row}")
                    print(f"Skipping row: {row}")
            print(f"--- Finished loading data ---")

    except FileNotFoundError:
        print(f"Error: Input file '{filepath}' not found. Please ensure 'results/top_customers_cleaned.csv' exists.")
        print("You might need to run the 'transform.py' script first to generate this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    cleaned_data_path = 'results/top_customers_cleaned.csv'

    load_and_print_customers(cleaned_data_path)