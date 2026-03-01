from amadeus import Client, ResponseError
from config import API_KEY, API_SECRET

amadeus = Client(
    client_id=API_KEY,
    client_secret=API_SECRET
)

def confirm_price(flight_offer):
    """Step 2 - Confirm the price is still available"""
    try:
        response = amadeus.shopping.flight_offers.pricing.post(
            flight_offer
        )
        return response.data
    except ResponseError as error:
        print("Price confirmation failed:", error)
        return None


def book_flight(flight_offer, passenger_details):
    """Step 3 - Create the actual booking"""
    try:
        response = amadeus.booking.flight_orders.post(
            flight_offer,
            passenger_details
        )
        return response.data
    except ResponseError as error:
        print("Booking failed:", error)
        return None


def build_passenger(first_name, last_name, dob, gender, email, phone, document_number):
    """Build passenger object in Amadeus format"""
    return {
        "id": "1",
        "dateOfBirth": dob,
        "name": {
            "firstName": first_name,
            "lastName": last_name
        },
        "gender": gender,
        "contact": {
            "emailAddress": email,
            "phones": [{
                "deviceType": "MOBILE",
                "countryCallingCode": "91",
                "number": phone
            }]
        },
        "documents": [{
            "documentType": "PASSPORT",
            "birthPlace": "India",
            "issuanceLocation": "India",
            "issuanceDate": "2020-01-01",
            "number": document_number,
            "expiryDate": "2030-01-01",
            "issuanceCountry": "IN",
            "validityCountry": "IN",
            "nationality": "IN",
            "holder": True
        }]
    }


# Test
if __name__ == "__main__":
    print("Booking module ready!")
    print("Passenger builder test:")
    passenger = build_passenger(
        first_name="Sudhanshu",
        last_name="Bhawsar",
        dob="1995-01-01",
        gender="MALE",
        email="test@gmail.com",
        phone="9999999999",
        document_number="A1234567"
    )
    import json
    print(json.dumps(passenger, indent=2))


if __name__ == "__main__":
    from amadeus import Client, ResponseError
    from config import API_KEY, API_SECRET

    amadeus = Client(client_id=API_KEY, client_secret=API_SECRET)

    # Search
    flights = amadeus.shopping.flight_offers_search.get(
        originLocationCode='DEL',
        destinationLocationCode='BOM',
        departureDate='2026-03-15',
        adults=1
    ).data

    cheapest = min(flights, key=lambda x: float(x['price']['total']))

    # Confirm price
    confirmed = amadeus.shopping.flight_offers.pricing.post(cheapest).data
    flight_offer = confirmed['flightOffers'][0]

    # Build passenger
    passenger = build_passenger(
        first_name="Sudhanshu",
        last_name="Bhawsar",
        dob="1995-01-01",
        gender="MALE",
        email="test@gmail.com",
        phone="9999999999",
        document_number="A1234567"
    )

    # Book
    result = book_flight(flight_offer, [passenger])
    if result:
        print("Booking successful!")
        print(result)
    else:
        print("Booking failed!")