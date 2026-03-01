# ✈️ Flight Price Watcher & Auto Booker

A Python web app that tracks flight prices and automatically books when the price hits your target — like a stock market limit order, but for flights!

## 🚀 Features

- Search flights using Amadeus API
- Set a target price and get alerted when price drops
- Auto price watcher that checks prices automatically every X seconds
- Price history tracking saved to CSV
- Live price trend chart
- **Complete flight booking system with passenger details**
- **3 step booking flow — Search → Confirm Price → Book**
- **Booking confirmation with reference number**
- Clean web UI built with Streamlit

## 🛠️ Tech Stack

- Python 3.13
- Streamlit — Web UI
- Amadeus API — Flight data & booking
- Pandas — Data tracking and analysis
- Git & GitHub — Version control

## 📦 Installation

1. Clone the repository
   git clone git@github.com:sudhanshubhawsar-dev/flight-price-watcher.git
   cd flight-price-watcher

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install amadeus streamlit requests pandas

4. Add your Amadeus API keys
   Create a config.py file
   API_KEY = "your_api_key_here"
   API_SECRET = "your_api_secret_here"

5. Run the app
   streamlit run app.py

## 📁 Project Structure

flight_watcher/
├── app.py              # Main Streamlit UI
├── flight_checker.py   # Amadeus API integration & flight search
├── price_tracker.py    # Price history tracking & CSV storage
├── watcher.py          # Auto price watcher loop
├── booking.py          # Flight booking & passenger management
├── config.py           # API keys (not pushed to GitHub)
├── price_history.csv   # Price history data
└── README.md           # Project documentation

## ✈️ How Booking Works

The booking follows the official Amadeus 3 step flow:

Step 1 — Flight Search
Search available flights for your route and date.

Step 2 — Price Confirmation
Confirm the price is still available before booking.

Step 3 — Flight Order Creation
Submit passenger details and create the booking.
Receive a booking ID and reference number instantly.

## 🗺️ Roadmap

- [x] Phase 1 — Flight search and price tracking
- [x] Phase 1.5 — Auto price watcher
- [x] Phase 2 — Complete flight booking system
- [ ] Phase 3 — Data analysis and price patterns
- [ ] Phase 4 — AI price prediction model
- [ ] Phase 5 — Auto booking when target price is hit

## 👨‍💻 Author

Sudhanshu Bhawsar
Aspiring Data & AI Developer
GitHub: sudhanshubhawsar-dev