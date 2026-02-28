# ✈️ Flight Price Watcher

A Python web app that tracks flight prices and alerts you when the price hits your target — like a stock market limit order, but for flights!

## 🚀 Features

- Search flights using Amadeus API
- Set a target price and get alerted when price drops
- Auto price watcher that checks prices automatically every X seconds
- Price history tracking saved to CSV
- Live price trend chart
- Clean web UI built with Streamlit

## 🛠️ Tech Stack

- Python 3.13
- Streamlit — Web UI
- Amadeus API — Flight data
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
├── flight_checker.py   # Amadeus API integration
├── price_tracker.py    # Price history tracking
├── watcher.py          # Auto price watcher
├── config.py           # API keys (not pushed to GitHub)
├── price_history.csv   # Price history data
└── README.md           # Project documentation

## 🗺️ Roadmap

- [x] Phase 1 — Flight search and price tracking
- [ ] Phase 2 — Data analysis and price patterns
- [ ] Phase 3 — AI price prediction model
- [ ] Phase 4 — Auto booking when target is hit

## 👨‍💻 Author

Sudhanshu Bhawsar
Aspiring Data & AI Developer
GitHub: sudhanshubhawsar-dev