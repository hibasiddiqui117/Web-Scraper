import csv
import json
import os
import pandas as pd

def save_data(data, file_path, format_='csv'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if format_ == 'csv':
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    elif format_ == 'json':
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    elif format_ == 'excel':
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False)
