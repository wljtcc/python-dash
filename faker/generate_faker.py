import csv
from faker import Faker
import random

# Seed for reproducibility
random.seed(42)

# Create Faker instance
fake = Faker()

# Function to generate random data
def generate_random_data():
    product = fake.word()
    quantity = random.randint(1, 10)
    sale_date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
    customer = fake.name()
    city = fake.city()
    state = fake.state_abbr()
    unit_price = round(random.uniform(10, 100), 2)  # Random unit price between 10 and 100
    total_value = round(quantity * unit_price, 2)

    return [product, quantity, sale_date, customer, city, state, unit_price, total_value]

# Number of records to generate
num_records = 10000

# CSV file path
csv_file_path = "random_sales_data.csv"

# Generate and write random data to CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header
    csv_writer.writerow(["Product", "Quantity", "Sale Date", "Customer", "City", "State", "Unit Price", "Total Value"])

    # Write random data
    for _ in range(num_records):
        csv_writer.writerow(generate_random_data())

print(f"CSV file generated: {csv_file_path}")
