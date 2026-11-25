
# Web Scraping - Product Information

A Python-based web scraping project that extracts product information from the Books to Scrape website and stores the collected data in a CSV file.

This project demonstrates how to collect structured information from a website using Python web scraping libraries.

## Features

- Scrape product names
- Extract product prices
- Extract product ratings
- Navigate through multiple pages automatically
- Save scraped data into a CSV file
- Handle HTTP request errors
- Use a delay between requests

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV
- HTML Parsing

## Website Used

Books to Scrape:

https://books.toscrape.com/

This website is designed for practicing web scraping.

## Requirements

- Python 3.x
- Requests
- BeautifulSoup4

## Installation

Install the required Python libraries:

```bash
python -m pip install requests beautifulsoup4
```

## Project Structure

```text
Task_05_Web_Scraping/
│
├── main.py
├── README.md
└── products.csv
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Task_05_Web_Scraping.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Task_05_Web_Scraping
   ```

3. Install dependencies:

   ```bash
   python -m pip install requests beautifulsoup4
   ```

4. Run the program:

   ```bash
   python main.py
   ```

## Output

The program collects product information from the website and generates a CSV file named:

`products.csv`

The CSV file contains the following columns:

- Product Name
- Price
- Rating

## Learning Outcomes

- Understanding web scraping
- Sending HTTP requests using Python
- Parsing HTML using BeautifulSoup
- Extracting data from HTML elements
- Handling pagination
- Working with CSV files
- Handling request errors

## Internship Task

Task 05 completed as part of the Software Development Internship Program at Prodigy InfoTech.

## Author

Hasrat Shaikh

GitHub: https://github.com/hasratshaikh
