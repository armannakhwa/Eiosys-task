import sqlite3

# Create a SQLite database and establish a connection
connection = sqlite3.connect("customer_orders.db")
cursor = connection.cursor()

# Create Customers table
cursor.execute('''CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)''')

# Create Orders table
cursor.execute('''CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    order_value INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)''')
connection.commit()
connection.close()
