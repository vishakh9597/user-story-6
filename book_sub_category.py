import requests
from bs4 import BeautifulSoup
import csv
import logging
from urllib.parse import urljoin

logging.basicConfig(
    level=logging.INFO,
    format="SCRAPER | %(levelname)s | %(message)s"
)

BASE_URL = "http://books.toscrape.com/"
OUTPUT_FILE = "books_data.csv"

def get_rating(rating_class):
    rating_map = {
        "One": 1, "Two": 2, "Three": 3,
        "Four": 4, "Five": 5
    }
    return rating_map.get(rating_class, None)


def get_subcategories():
    """Scrape all subcategories from sidebar"""
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    categories = []

    category_links = soup.select(".side_categories ul li ul li a")

    for category in category_links:
        name = category.text.strip()
        relative_url = category.get("href")
        full_url = urljoin(BASE_URL, relative_url)

        categories.append((name, full_url))

    return categories


def scrape_books():
    logging.info("Book scraping started")

    books = []
    categories = get_subcategories()

    for category_name, category_url in categories:
        logging.info(f"Scraping category: {category_name}")
        url = category_url

        while url:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"HTTP Error while accessing {url}: {e}")
                break

            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.select("article.product_pod")

            for index, book in enumerate(articles, start=1):
                try:
                    title = book.h3.a["title"]
                    price = book.select_one(".price_color").text.replace("£", "")
                    availability = book.select_one(".availability").text.strip()
                    rating_class = book.p["class"][1]
                    rating = get_rating(rating_class)
                    product_url = urljoin(url, book.h3.a["href"])

                    books.append([
                        title,
                        price,
                        rating,
                        availability,
                        category_name,   # ✅ Subcategory added
                        product_url
                    ])

                except Exception as e:
                    logging.warning(f"Skipping book due to error: {e}")

            # Pagination inside category
            next_page = soup.select_one("li.next a")
            if next_page:
                url = urljoin(url, next_page["href"])
            else:
                url = None

    logging.info(f"Total books scraped successfully: {len(books)}")
    save_to_csv(books)


def save_to_csv(data):
    logging.info("Saving data to CSV file")

    try:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Title",
                "Price_GBP",
                "Rating",
                "Availability",
                "Subcategory",
                "URL"
            ])
            writer.writerows(data)

        logging.info(f"CSV file '{OUTPUT_FILE}' saved successfully")

    except Exception as e:
        logging.error(f"Error while saving CSV file: {e}")


if __name__ == "__main__":
    logging.info("Scraper execution started")
    scrape_books()
    logging.info("Scraper execution finished")
