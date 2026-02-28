import time
import streamlit as st
from flight_checker import get_all_parsed_flights
from price_tracker import save_price, load_history

def watch_prices(origin, destination, date, target_price, interval_seconds=60, max_checks=10):
    """
    Watches flight prices every `interval_seconds`.
    Stops when price hits target or max_checks is reached.
    """
    print(f"\n🔍 Watching prices for {origin} → {destination} on {date}")
    print(f"🎯 Target Price: {target_price} EUR")
    print(f"⏱️  Checking every {interval_seconds} seconds\n")

    for check in range(1, max_checks + 1):
        print(f"Check #{check} of {max_checks}...")

        flights = get_all_parsed_flights(origin, destination, date)

        if not flights:
            print("No flights found. Retrying...")
            time.sleep(interval_seconds)
            continue

        cheapest = min(flights, key=lambda x: x['price'])
        current_price = cheapest['price']
        currency = cheapest['currency']

        # Save to history
        save_price(origin, destination, date, current_price, currency)

        print(f"💰 Current cheapest price: {current_price} {currency}")

        if current_price <= target_price:
            print(f"\n🎉 TARGET HIT! Price {current_price} {currency} is at or below your target {target_price} EUR!")
            return True, current_price

        else:
            diff = round(current_price - target_price, 2)
            print(f"⏳ Still {diff} EUR above target. Next check in {interval_seconds} seconds...\n")
            time.sleep(interval_seconds)

    print(f"\n⚠️ Max checks reached. Target price not hit.")
    return False, None


# Test
if __name__ == "__main__":
    hit, price = watch_prices(
        origin='DEL',
        destination='BOM',
        date='2026-03-15',
        target_price=100.0,
        interval_seconds=10,  # 10 seconds for testing
        max_checks=3
    )

    if hit:
        print(f"✅ Book now at {price} EUR!")
    else:
        print("❌ Target not reached yet.")