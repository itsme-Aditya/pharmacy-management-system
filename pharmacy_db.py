import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect('pharmacy_data.db', check_same_thread=False)
c = conn.cursor()

# Create Drugs Table
def create_drug_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Drugs(
                D_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                D_Name TEXT NOT NULL,
                D_ExpiryDate DATE NOT NULL,
                D_Use TEXT NOT NULL,
                D_Qty INTEGER NOT NULL,
                D_Price REAL NOT NULL)
                ''')
    conn.commit()

# Create Customers Table
def create_customer_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Customers(
                C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                C_Name TEXT NOT NULL,
                C_Email TEXT UNIQUE NOT NULL,
                C_Phone TEXT NOT NULL)
                ''')
    conn.commit()

# Create Orders Table
def create_order_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Orders(
                O_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                C_ID INTEGER NOT NULL,
                D_ID INTEGER NOT NULL,
                O_Qty INTEGER NOT NULL,
                O_Total REAL NOT NULL,
                O_Date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(C_ID) REFERENCES Customers(C_ID),
                FOREIGN KEY(D_ID) REFERENCES Drugs(D_ID))
                ''')
    conn.commit()

# Initialize all tables
def init_db():
    create_drug_table()
    create_customer_table()
    create_order_table()

# Add Drug
def add_drug(name, expiry_date, use, qty, price):
    c.execute('''INSERT INTO Drugs (D_Name, D_ExpiryDate, D_Use, D_Qty, D_Price)
                 VALUES (?, ?, ?, ?, ?)''', (name, expiry_date, use, qty, price))
    conn.commit()

# Add Customer
def add_customer(name, email, phone):
    c.execute('''INSERT INTO Customers (C_Name, C_Email, C_Phone)
                 VALUES (?, ?, ?)''', (name, email, phone))
    conn.commit()

# Add Order
def add_order(customer_id, drug_id, qty, total):
    c.execute('''INSERT INTO Orders (C_ID, D_ID, O_Qty, O_Total)
                 VALUES (?, ?, ?, ?)''', (customer_id, drug_id, qty, total))
    conn.commit()

# Update Drug Quantity
def update_drug_quantity(drug_id, new_quantity):
    c.execute('''UPDATE Drugs SET D_Qty = ? WHERE D_ID = ?''', (new_quantity, drug_id))
    conn.commit()

# View Drugs
def view_drugs():
    c.execute('SELECT * FROM Drugs')
    return c.fetchall()

# View Customers
def view_customers():
    c.execute('SELECT * FROM Customers')
    return c.fetchall()

# View Orders
def view_orders():
    c.execute('''SELECT O.O_ID, C.C_Name, D.D_Name, O.O_Qty, O.O_Total, O.O_Date 
                 FROM Orders O
                 JOIN Customers C ON O.C_ID = C.C_ID
                 JOIN Drugs D ON O.D_ID = D.D_ID''')
    return c.fetchall()

