from scraper.config_loader import load_config
from scraper.fetcher import fetch_page
from scraper.selector_engine import extract_data
from scraper.saver import save_data
from scraper.utils import setup_logging


def main():
    setup_logging()
    print("🚀 Universal Web Scraper Starting...\n")

    # Load config file
    config = load_config("configs/openlibrary_config.yaml")


    base_url = config["base_url"]
    start_page = config["start_page"]
    end_page = config["end_page"]
    container = config["selectors"]["container"]
    fields = config["selectors"]["fields"]
    output_path = config["output"]["file_path"]
    output_format = config["output"]["format"]

    all_data = []

    for page in range(start_page, end_page + 1):
        url = base_url.format(page=page)
        print(f"🔍 Scraping Page {page}: {url}")

        html = fetch_page(url)

        if not html:
            print(f"❌ Page {page} could not be fetched. Skipping...\n")
            continue

        extracted = extract_data(html, container, fields)

        if extracted:
            print(f"✅ Page {page}: Extracted {len(extracted)} item(s).")
            all_data.extend(extracted)
        else:
            print(f"⚠️ Page {page}: No matching data found.\n")

    if all_data:
        save_data(all_data, output_path, output_format)
        print(f"\n✅ Scraping Complete! {len(all_data)} items saved to '{output_path}'.")
    else:
        print("\n⚠️ Scraping ended with no data extracted. Please check your CSS selectors or page structure.")

    print("\n🔚 Scraper Finished.")

if __name__ == "__main__":
    main()
