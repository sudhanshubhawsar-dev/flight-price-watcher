import streamlit as st
import pandas as pd
from datetime import date
from flight_checker import get_all_parsed_flights
from price_tracker import save_price, load_history
import time

# Page config
st.set_page_config(page_title="Flight Price Watcher", page_icon="✈️", layout="wide")

st.title("✈️ Flight Price Watcher")
st.markdown("Search flights and watch for your target price!")

# --- Input Section ---
st.subheader("🔍 Search Flights")

col1, col2 = st.columns(2)

with col1:
    origin = st.text_input("From (IATA Code)", value="DEL", max_chars=3).upper()
    departure_date = st.date_input("Departure Date", min_value=date.today())

with col2:
    destination = st.text_input("To (IATA Code)", value="BOM", max_chars=3).upper()
    adults = st.number_input("Passengers", min_value=1, max_value=9, value=1)

target_price = st.number_input("🎯 Your Target Price (EUR)", min_value=0.0, value=100.0, step=5.0)

search_btn = st.button("Search Flights", type="primary")

# --- Results Section ---
if search_btn:
    with st.spinner("Searching flights..."):
        flights = get_all_parsed_flights(origin, destination, str(departure_date), adults)

    if not flights:
        st.error("No flights found. Try different dates or routes.")
    else:
        cheapest = min(flights, key=lambda x: x['price'])
        current_price = cheapest['price']

        # Save price to history
        save_price(origin, destination, str(departure_date), current_price, cheapest['currency'])

        st.subheader("📊 Results")

        # Metrics row
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Flights Found", len(flights))
        col2.metric("Cheapest Price", f"{current_price} {cheapest['currency']}")
        col3.metric("Your Target Price", f"{target_price} EUR")

        # Alert
        if current_price <= target_price:
            st.success(f"🎉 Great news! Current price ({current_price} EUR) is at or below your target ({target_price} EUR)! Book now!")
        else:
            diff = round(current_price - target_price, 2)
            st.warning(f"⏳ Price is {diff} EUR above your target. Keep watching!")

        # Cheapest flight details
        st.subheader("🏆 Cheapest Flight")
        detail_col1, detail_col2 = st.columns(2)
        with detail_col1:
            st.write(f"✈️ **Airline:** {cheapest['airline']}")
            st.write(f"🛫 **Departure:** {cheapest['departure_time']}")
            st.write(f"🛬 **Arrival:** {cheapest['arrival_time']}")
            st.write(f"⏱️ **Duration:** {cheapest['duration']}")
        with detail_col2:
            st.write(f"🔁 **Stops:** {cheapest['stops']}")
            st.write(f"💺 **Cabin:** {cheapest['cabin']}")
            st.write(f"🧳 **Baggage:** {cheapest['baggage_kg']} KG")
            st.write(f"💺 **Seats Available:** {cheapest['seats_available']}")

        # All flights table
        st.subheader("📋 All Flights")
        df = pd.DataFrame(flights)
        df = df.sort_values('price')
        st.dataframe(df, use_container_width=True)


# --- Auto Watcher Section ---
st.divider()
st.subheader("🤖 Auto Price Watcher")
st.markdown("Set it and forget it! The watcher will automatically check prices for you.")

col1, col2 = st.columns(2)
with col1:
    interval = st.number_input("Check every (seconds)", min_value=10, max_value=3600, value=30)
with col2:
    max_checks = st.number_input("Maximum checks", min_value=1, max_value=100, value=5)

watch_btn = st.button("🚀 Start Watching", type="primary")

if watch_btn:
    st.info(f"👀 Watching {origin} → {destination} every {interval} seconds for up to {max_checks} checks...")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    result_placeholder = st.empty()

    for check in range(1, max_checks + 1):
        status_text.write(f"🔍 Check #{check} of {max_checks}...")
        
        flights = get_all_parsed_flights(origin, destination, str(departure_date), adults)
        
        if flights:
            cheapest = min(flights, key=lambda x: x['price'])
            current_price = cheapest['price']
            currency = cheapest['currency']

            save_price(origin, destination, str(departure_date), current_price, currency)

            if current_price <= target_price:
                result_placeholder.success(f"🎉 TARGET HIT! Price {current_price} {currency} is at or below your target {target_price} EUR! Book now!")
                progress_bar.progress(100)
                break
            else:
                diff = round(current_price - target_price, 2)
                result_placeholder.warning(f"⏳ Check #{check}: {current_price} {currency} — still {diff} EUR above target.")
        
        progress_bar.progress(int((check / max_checks) * 100))
        
        if check < max_checks:
            time.sleep(interval)
    
    else:
        result_placeholder.error(f"⚠️ Finished {max_checks} checks. Target price not reached yet.")

    status_text.write("✅ Watching complete!")

# --- Price History Section ---
st.divider()
st.subheader("📈 Price History")

history = load_history(origin, destination)

if history.empty:
    st.info("No price history yet. Search for flights to start tracking!")
else:
    # Line chart
    st.line_chart(history.set_index('timestamp')['price'])

    # History table
    st.subheader("🗂️ History Log")
    st.dataframe(history, use_container_width=True)