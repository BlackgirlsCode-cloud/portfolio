"""
segment_donors.py
Categorizes donors into Low, Medium, and High segments based on donation amounts.

Author: [Your Name]
"""

import pandas as pd

def segment_donors(input_file: str, output_file: str):
    """Adds a donor segment column and saves to new file."""
    try:
        df = pd.read_csv(input_file)
        print(f"Loaded {len(df)} rows from {input_file}")

        # Create segments based on donation amount quantiles
        df['segment'] = pd.qcut(df['donation_amount'], q=3, labels=['Low', 'Medium', 'High'])

        df.to_csv(output_file, index=False)
        print(f"✅ Donors segmented and saved to {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    segment_donors("cleaned_donors.csv", "segmented_donors.csv")
