import sqlite3

# Define the database file path
stock_database = 'stock_database.db'

# Define the SQL statements to create tables
CREATE_STOCK_TABLE = '''
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY,
        item_name TEXT NOT NULL,
        quantity INTEGER,
        price REAL
    )
'''

CREATE_SALES_TABLE = '''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        item_id INTEGER,
        quantity_sold INTEGER,
        total_price REAL,
        FOREIGN KEY (item_id) REFERENCES stock (id)
    )
'''

# Function to create database tables
def create_tables():
    try:
        with sqlite3.connect(stock_database) as conn:
            cursor = conn.cursor()
            cursor.execute(CREATE_STOCK_TABLE)
            cursor.execute(CREATE_SALES_TABLE)
        print("Tables created successfully")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

# Call the function to create tables
create_tables()