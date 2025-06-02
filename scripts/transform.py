import csv
import os

def format_nigerian_currency(amount):
    try:
        numeric_amount = float(amount)
        formatted_amount = f"{numeric_amount:,.2f}"
        return f"₦{formatted_amount}"
    except (ValueError, TypeError):
        return str(amount) # Return original if conversion fails


def clean_customer_data(input_filepath, output_filepath):

    output_dir = os.path.dirname(output_filepath)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(input_filepath, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            # Read header row
            header = next(reader) 

            try:
                customer_name_idx = header.index('customer_name')
                total_spent_idx = header.index('total_spent')
            except ValueError as e:
                print(f"Error: Missing expected column in CSV header: {e}")
                print(f"Header found: {header}")
                return

            with open(output_filepath, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                # Write the header to the output file
                writer.writerow(header) 

                for row in reader:
                    if len(row) > max(customer_name_idx, total_spent_idx):
                        # Convert customer name to title case
                        row[customer_name_idx] = str(row[customer_name_idx]).title()
                        # Format total_spent as Nigerian currency
                        row[total_spent_idx] = format_nigerian_currency(row[total_spent_idx])
                    else:
                        print(f"Warning: unable to clean row: {row}")
                        print(f"...Skipping row: {row}")
                    writer.writerow(row)

        print(f"Successfully cleaned data from '{input_filepath}' and saved to '{output_filepath}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found. Please ensure it exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":

    input_path = 'results/top_customers.csv'
    if not os.path.exists('results'):
        os.makedirs('results')

    clean_customer_data('results/top_customers.csv', 'results/top_customers_cleaned.csv')