
import csv
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = Path(__file__).parent / "products.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; StudentWebScraper/1.0)"
}

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def scrape_page(url):
    """Scrape product information from one page."""

    print(f"Scraping: {url}")

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        response.raise_for_status()

    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    product_cards = soup.select("article.product_pod")

    for card in product_cards:
        # Product name
        title_element = card.select_one("h3 a")

        if title_element:
            product_name = title_element.get("title", "").strip()
        else:
            product_name = "Unknown"

        # Product price
        price_element = card.select_one(".price_color")

        if price_element:
            product_price = price_element.get_text(strip=True)
        else:
            product_price = "N/A"

        # Product rating
        rating_element = card.select_one(".star-rating")

        if rating_element:
            rating_classes = rating_element.get("class", [])
            rating_word = next(
                (
                    class_name
                    for class_name in rating_classes
                    if class_name in RATING_MAP
                ),
                None
            )

            product_rating = RATING_MAP.get(
                rating_word,
                "N/A"
            )
        else:
            product_rating = "N/A"

        products.append({
            "Product Name": product_name,
            "Price": product_price,
            "Rating": product_rating
        })

    # Find the next page link
    next_element = soup.select_one("li.next a")

    if next_element:
        next_url = urljoin(url, next_element.get("href"))
    else:
        next_url = None

    return products, next_url


def save_to_csv(products):
    """Save scraped products to a CSV file."""

    if not products:
        print("No product data available to save.")
        return

    fieldnames = [
        "Product Name",
        "Price",
        "Rating"
    ]

    try:
        with open(
            OUTPUT_FILE,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as csv_file:

            writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(products)

        print(f"\nData saved successfully to: {OUTPUT_FILE}")

    except OSError as error:
        print(f"Error saving CSV file: {error}")


def main():
    """Run the web scraping application."""

    print("=" * 50)
    print("       PRODUCT INFORMATION WEB SCRAPER")
    print("=" * 50)

    all_products = []
    current_url = BASE_URL
    page_number = 1

    while current_url:
        products, next_url = scrape_page(current_url)

        if not products:
            print("No products found on this page.")
            break

        all_products.extend(products)

        print(
            f"Page {page_number}: "
            f"{len(products)} products collected."
        )

        current_url = next_url
        page_number += 1

        # Pause between requests to avoid sending them too quickly
        if current_url:
            time.sleep(0.5)

    print("\n" + "=" * 50)
    print(f"Total products scraped: {len(all_products)}")
    print("=" * 50)

    save_to_csv(all_products)


if __name__ == "__main__":
    main()
