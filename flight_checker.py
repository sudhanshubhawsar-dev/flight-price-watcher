from amadeus import Client, ResponseError
from config import API_KEY, API_SECRET

amadeus = Client(
    client_id=API_KEY,
    client_secret=API_SECRET
)

def search_flights(origin, destination, date, adults=1):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=adults
        )
        return response.data
    except ResponseError as error:
        print("Error fetching flights:", error)
        return []

def parse_flight(flight):
    segments = flight['itineraries'][0]['segments']
    first_segment = segments[0]
    last_segment = segments[-1]
    fare_details = flight['travelerPricings'][0]['fareDetailsBySegment'][0]

    return {
        'price': float(flight['price']['total']),
        'currency': flight['price']['currency'],
        'origin': first_segment['departure']['iataCode'],
        'destination': last_segment['arrival']['iataCode'],
        'departure_time': first_segment['departure']['at'],
        'arrival_time': last_segment['arrival']['at'],
        'duration': flight['itineraries'][0]['duration'],
        'stops': len(segments) - 1,
        'airline': first_segment['carrierCode'],
        'seats_available': flight['numberOfBookableSeats'],
        'cabin': fare_details['cabin'],
        'baggage_kg': fare_details['includedCheckedBags']['weight']
    }

def get_cheapest_price(flights):
    if not flights:
        return None
    prices = [float(f['price']['total']) for f in flights]
    return min(prices)

def get_all_parsed_flights(origin, destination, date, adults=1):
    flights = search_flights(origin, destination, date, adults)
    return [parse_flight(f) for f in flights]


# Test
if __name__ == "__main__":
    flights = get_all_parsed_flights('DEL', 'BOM', '2026-03-15')
    print(f"Total flights: {len(flights)}")
    print("\nCheapest flight details:")
    cheapest = min(flights, key=lambda x: x['price'])
    for key, value in cheapest.items():
        print(f"  {key}: {value}")