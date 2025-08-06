import requests
import logging

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Fetched: {url}")
        return response.text
    except Exception as e:
        logging.error(f"Error fetching {url}: {e}")
        return None
