import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Number of records to generate
num_records = 1000

# List to hold generated data
transactions = []

for _ in range(num_records):
    transaction = {
        "application_id": fake.random_number(digits=18, fix_len=True),
        "arn": fake.random_number(digits=9, fix_len=True),
        "card_number": fake.credit_card_number(card_type="visa"),
        "customer_id": fake.random_number(digits=11, fix_len=True),
        "transaction_datetime": fake.date_time_between(start_date="-1y", end_date="now"),
        "transaction_amount": round(random.uniform(10.0, 5000.0), 2),
        "description": fake.sentence(nb_words=5)
    }
    transactions.append(transaction)

# Create DataFrame
df = pd.DataFrame(transactions)

# Format transaction_amount with commas
df["transaction_amount"] = df["transaction_amount"].map("{:,}".format)

# Save to CSV
df.to_csv("storage/credit_card_transactions.csv", index=False)

print(df.head(5))
print(f"Generated {num_records} credit card transactions.")
