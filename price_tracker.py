import pandas as pd
import os
from datetime import datetime

HISTORY_FILE = 'price_history.csv'

def save_price(origin, destination, date, price, currency):
    # Create a new record
    new_record = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'origin': origin,
        'destination': destination,
        'date': date,
        'price': price,
        'currency': currency
    }

    # If file exists, load it and append — otherwise create new
    if os.path.exists(HISTORY_FILE):
        df = pd.read_csv(HISTORY_FILE)
        new_row = pd.DataFrame([new_record])
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = pd.DataFrame([new_record])

    # Save back to CSV
    df.to_csv(HISTORY_FILE, index=False)
    print(f"Price saved: {price} {currency}")

def load_history(origin, destination):
    if not os.path.exists(HISTORY_FILE):
        return pd.DataFrame()  # Empty dataframe if no history yet

    df = pd.read_csv(HISTORY_FILE)

    # Filter by route
    filtered = df[(df['origin'] == origin) & (df['destination'] == destination)]
    return filtered


# Test
if __name__ == "__main__":
    save_price('DEL', 'BOM', '2026-03-15', 66.62, 'EUR')
    save_price('DEL', 'BOM', '2026-03-15', 70.10, 'EUR')
    save_price('DEL', 'BOM', '2026-03-15', 63.20, 'EUR')

    history = load_history('DEL', 'BOM')
    print(history)