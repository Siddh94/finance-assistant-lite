import requests
from bs4 import BeautifulSoup
from typing import List

def scrape_yahoo_earnings(symbol: str) -> List[str]:
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"[Scraper] Failed to fetch data for {symbol}: HTTP {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")
        news_items = soup.select('li.js-stream-content h3')

        earnings_news = [
            item.text.strip() for item in news_items
            if any(w in item.text.lower() for w in ["earnings", "q1", "q2", "q3", "q4", "profit", "report"])
        ]

        if not earnings_news:
            print(f"[Scraper] No earnings headlines found for {symbol}")

        return earnings_news

    except Exception as e:
        print(f"[Scraper] Exception while scraping {symbol}: {e}")
        return []
