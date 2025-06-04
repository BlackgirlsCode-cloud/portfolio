"""
generate_emails.py
Generates thank-you email messages for donors based on their donation segment.

Author: [Your Name]
"""

import pandas as pd

def generate_emails(input_file: str):
    """Prints email messages for each donor in the file."""
    try:
        df = pd.read_csv(input_file)

        for _, row in df.iterrows():
            name = row.get('name', 'Donor')
            segment = row.get('segment', 'Supporter')
            email = row.get('email', '')

            message = (
                f"To: {email}\n"
                f"Subject: Thank You for Your Generous Support\n\n"
                f"Dear {name},\n\n"
                f"Thank you for being a valued {segment} donor. "
                f"Your contribution helps us continue our mission.\n\n"
                f"Warm regards,\nYour Organization\n"
            )
            print(message)
            print("-" * 50)

        print("✅ All donor emails generated.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_emails("segmented_donors.csv")
