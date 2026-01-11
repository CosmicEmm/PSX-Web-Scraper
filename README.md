# PSX Web Scraper & Data Logger

A Python-based web scraping project that automatically extracts real-time KSE-100 index data from the Pakistan Stock Exchange (PSX) and logs it into a structured CSV dataset for analysis. This project demonstrates data collection, automation, and analysis workflows from web scraping to data storage and visualization-ready output using Python’s data ecosystem.

## Features

- Automated Scraping: Continuously fetches live KSE-100 index data at fixed time intervals.
- Real-Time Tracking: Captures index value and percentage change from PSX.
- Time Logging: Records timestamps to enable time-series trend analysis.
- CSV Export: Stores clean, structured data for later analysis or visualization.
- Error Handling: Handles connection and parsing errors gracefully for reliability.

## Skills Demonstrated

- Web Scraping with BeautifulSoup and Requests
- Data Collection & Cleaning with Pandas
- Data Automation & Scheduling using loops and time intervals
- Data Storage in CSV format
- Documentation & Version Control using Git and GitHub

## Project Architecture

```
PSX Web Scraper
│
├── PSXWebScraper.ipynb       # Jupyter Notebook version (for experimentation)
├── psx_scraper.py            # Python script version (for continuous logging)
├── PSXWebScraperDataset.csv  # Generated dataset (sample data)
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

## Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/<your-username>/PSX-Web-Scraper.git
cd PSX-Web-Scraper
```

2. Install Required Libraries
```bash
pip install -r requirements.txt
```

3. Run the Scraper
```bash
python psx_scraper.py
```

The script will fetch the latest KSE-100 index data every 10 seconds and append it to PSXWebScraperDataset.csv.

To stop it, press Ctrl + C in the terminal.

## Author

Muhammad

📍 Data Analyst | Python Programmer | Data Explorer

🔗 [LinkedIn Profile](https://www.linkedin.com/in/emmmuhammad/)
