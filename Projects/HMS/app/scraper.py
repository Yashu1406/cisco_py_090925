import requests
from bs4 import BeautifulSoup
from app.logger import logger

def scrape_hospital_info(url: str) -> dict:
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        info = {}
        # Example: scrape departments (assuming <li class="department">...</li>)
        departments = [li.text.strip() for li in soup.select("li.department")]
        info["departments"] = departments
        logger.info(f"Scraped hospital info from {url}")
        return info
    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        return {}