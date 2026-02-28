from amadeus import Client, ResponseError

from config import API_KEY, API_SECRET

amadeus = Client(
    client_id=API_KEY,
    client_secret=API_SECRET
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='DEL',
        destinationLocationCode='BOM',
        departureDate='2026-03-15',
        adults=1
    )
    print("Connection Successful!")
    print(f"Found {len(response.data)} flights")
except ResponseError as error:
    print("Connection Failed:", error)