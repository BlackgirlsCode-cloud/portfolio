"""
scrape_events.py
Scrapes event data (titles and dates) from a sample event website and saves it to a CSV.

Author: [Your Name]
"""

import requests
from bs4 import BeautifulSoup
import csv

def scrape_event_data(url: str, output_file: str):
    """Scrapes events from the given URL and saves them to a CSV file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # These selectors are placeholders; update them for a real site
        events = soup.select('.event-card')
        event_list = []

        for item in events:
            title = item.select_one('.event-title').get_text(strip=True)
            date = item.select_one('.event-date').get_text(strip=True)
            event_list.append([title, date])

        # Save to CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Date'])
            writer.writerows(event_list)

        print(f"✅ Scraped {len(event_list)} events to {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Replace with a real event URL when testing
    scrape_event_data("https://example.com/events", "events.csv")
