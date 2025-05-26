import pandas as pd
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Load the CSV file using absolute path
input_path = os.path.join(project_root, 'Results', 'top_customers.csv')
df = pd.read_csv(input_path)

# Convert customer names to title case
df['customer_name'] = df['customer_name'].str.title()

# Format amount as Nigerian Naira (₦) with comma separators and two decimal places
df['total_spent'] = df['total_spent'].apply(lambda x: f"₦{x:,.2f}")

# Save the cleaned data to a new CSV file
output_path = os.path.join(project_root, 'Results', 'top_customers_cleaned.csv')
df.to_csv(output_path, index=False)

print(f"Cleaned data saved to: {output_path}")