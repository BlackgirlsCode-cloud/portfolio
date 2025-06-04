"""
clean_donors.py
Cleans donor data from a CSV file: removes duplicates, filters invalid donations,
and normalizes email addresses.

Author: [Your Name]
"""

import pandas as pd

def clean_donor_data(input_file: str, output_file: str):
    """Cleans donor data and saves the cleaned version to a new file."""
    try:
        df = pd.read_csv(input_file)
        print(f"Loaded {len(df)} rows from {input_file}")

        # Remove duplicates by email
        df = df.drop_duplicates(subset='email')

        # Normalize email addresses
        df['email'] = df['email'].str.lower().str.strip()

        # Filter out non-positive donation amounts
        df = df[df['donation_amount'] > 0]

        df.to_csv(output_file, index=False)
        print(f"✅ Cleaned data saved to {output_file} with {len(df)} valid rows.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    clean_donor_data("sample_data.csv", "cleaned_donors.csv")
# Script to clean donor data
