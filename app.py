from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def retrieve_top_customers():
    connection = sqlite3.connect("customer_orders.db")
    cursor = connection.cursor()
    
    query = """
        SELECT c.name, c.email, SUM(o.order_value) AS total_order_value
        FROM Customers c
        JOIN Orders o ON c.customer_id = o.customer_id
        WHERE o.order_date >= date('now', '-30 days')
        GROUP BY c.name, c.email
        HAVING COUNT(o.order_id) = 1
        ORDER BY total_order_value DESC
        LIMIT 10
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return results

@app.route('/top_customers')
def top_customers():
    customers = retrieve_top_customers()
    return render_template('results.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)
