"""
------------------------------------------------------------
PSX Web Scraper & Data Logger
------------------------------------------------------------
Author: Muhammad
Description:
    A Python-based scraper that collects real-time KSE-100 
    index data from the Pakistan Stock Exchange (PSX) website 
    and logs it into a CSV file for time-series analysis.
------------------------------------------------------------
"""

# =========================
# Import Required Libraries
# =========================
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv
import time
import pandas as pd

# =========================
# Constants
# =========================
URL = 'https://dps.psx.com.pk/'
csv_file = 'PSXWebScraperDataset.csv'
scrape_interval = 10  # seconds

# =========================
# Initial CSV Setup
# =========================
header = ['Time', 'Current Index', 'Percent Change']

# Create CSV file with header (if not already present)
try:
    with open(csv_file, 'x', newline='', encoding='UTF-8') as f:  # 'x' mode for exclusive creation; fails if file exists
        writer = csv.writer(f)
        writer.writerow(header)
    print(f"[INIT] CSV file '{csv_file}' initialized with header.\n")
except FileExistsError:
    print(f"[INIT] CSV file '{csv_file}' already exists. Skipping creation.\n")

# =========================
# Function: append_data()
# =========================
def append_data():
    """Fetch KSE-100 index data and append to CSV file."""
    try:
        # Fetch webpage content
        response = requests.get(URL)

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        kse100_text = soup.find("h1", class_="marketIndices__price").get_text(strip=True)

        # Extract index value and percentage change
        current_index = kse100_text[:10]
        percent_change = kse100_text[11:]
        current_time = datetime.now().strftime("%H:%M:%S")

        # Append to CSV
        data = [current_time, current_index, percent_change]
        with open(csv_file, 'a', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

        print(f"[{current_time}] Data appended successfully: {current_index} | {percent_change}")

    except Exception as e:
        print(f"[ERROR] {e}")


# =========================
# Main Script Execution
# =========================
if __name__ == "__main__":
    print("[START] PSX Web Scraper running...\nPress Ctrl + C to stop.")

    try:
        while True:
            append_data()
            time.sleep(scrape_interval)

    except KeyboardInterrupt:
        print("\n[STOP] Scraper stopped by user.")

    # Optional: Load final dataset for review
    try:
        df = pd.read_csv(csv_file)
        print("\n[SUMMARY] Latest data preview:\n")
        print(df.tail())  # Display last 5 rows of DataFrame
    except Exception as e:
        print(f"[ERROR] Could not load CSV: {e}")