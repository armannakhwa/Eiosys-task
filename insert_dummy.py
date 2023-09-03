import sqlite3

# Create a SQLite database and establish a connection
connection = sqlite3.connect("customer_orders.db")
cursor = connection.cursor()

# Insert sample data into the Customers table
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("John Doe", "john@example.com"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("Jane Smith", "jane@example.com"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("Arman", "contact@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("Ajay", "ajay@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("vijay", "vijay@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample1", "sample1@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample2", "sample2@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample3", "sample3@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample4", "sample4@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample5", "sample5@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample6", "sample6@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample7", "sample7@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample8", "sample8@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample9", "sample9@armannakhwa.cf"))
cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", ("sample10", "sample10@armannakhwa.cf"))

# Insert sample data into the Orders table
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (1, "2023-08-01", 5000))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (1, "2023-08-15", 3000))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (2, "2023-08-25", 7500))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (2, "2023-08-26", 200))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (3, "2023-08-28", 2000))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (3, "2023-08-27", 9000))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (4, "2023-08-26", 4500))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (4, "2023-08-27", 7000))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (5, "2023-08-27", 4200))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (6, "2023-08-20", 800))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (7, "2023-08-21", 4800))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (8, "2023-08-15", 6700))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (9, "2023-08-19", 20))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (10, "2023-08-7", 3200))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (11, "2023-08-6", 2020))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (12, "2023-08-14", 220))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (13, "2023-08-14", 990))
cursor.execute("INSERT INTO Orders (customer_id, order_date, order_value) VALUES (?, ?, ?)", (14, "2023-08-14", 290))

# Commit the changes and close the connection
connection.commit()
connection.close()
