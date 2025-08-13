from bs4 import BeautifulSoup

def extract_data(html, container_selector, field_selectors):
    soup = BeautifulSoup(html, 'html.parser')
    containers = soup.select(container_selector)
    results = []

    for element in containers:
        item = {}
        for key, selector in field_selectors.items():
            selected = element.select_one(selector)
            item[key] = selected.get_text(strip=True) if selected else None
        results.append(item)

    return results
