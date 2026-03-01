import sqlite3
from datetime import datetime

DB_FILE = 'flight_watcher.db'

def get_connection():
    return sqlite3.connect(DB_FILE)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id TEXT,
            reference TEXT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            origin TEXT,
            destination TEXT,
            departure_date TEXT,
            price REAL,
            currency TEXT,
            booked_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Tables created successfully!")

def save_booking(booking_id, reference, first_name, last_name, email, phone, origin, destination, departure_date, price, currency):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO bookings (booking_id, reference, first_name, last_name, email, phone, origin, destination, departure_date, price, currency)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (booking_id, reference, first_name, last_name, email, phone, origin, destination, departure_date, price, currency))
    
    conn.commit()
    conn.close()
    print(f"Booking saved: {reference}")

def get_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM bookings ORDER BY booked_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_booking_columns():
    return ['id', 'booking_id', 'reference', 'first_name', 'last_name', 'email', 'phone', 'origin', 'destination', 'departure_date', 'price', 'currency', 'booked_at']


# Test
if __name__ == "__main__":
    create_tables()
    
    save_booking(
        booking_id="TEST123",
        reference="ABCDEF",
        first_name="Sudhanshu",
        last_name="Bhawsar",
        email="test@gmail.com",
        phone="9999999999",
        origin="DEL",
        destination="BOM",
        departure_date="2026-03-15",
        price=68.69,
        currency="EUR"
    )
    
    bookings = get_all_bookings()
    print(f"\nTotal bookings: {len(bookings)}")
    for b in bookings:
        print(b)