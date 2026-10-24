import sqlite3 

#1. Connect to the database 
conn = sqlite3.connect('products.db')

#2. Create a cursor object to execute SQL commands
cursor = conn.cursor()


#3. Create a table to store product data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY ,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        warehouse INTEGER NOT NULL,
        status TEXT NOT NULL
    )''')

# Insert sample data into the products table
cursor.execute('''
    INSERT INTO products (id, name, price, stock, warehouse, status) VALUES
    (1001,'Wireless Mouse', 10.99, 100, 1, 'active'),
    (1002,'Wireless Mouse Pro', 20.99, 50, 2, 'active'),
    (1003,'Computer', 30.99, 25, 1, 'inactive')
''')

#Select all products from the table
cursor.execute('SELECT * FROM products')


# Fetch all rows from the result set
all_rows = cursor.fetchall()
# print(all_rows)

# Update a product's stock
stock = input("Enter stock:")
id = input("Enter id:")
cursor.execute('UPDATE products SET stock = ? WHERE id = ?', (stock, id))

#Delete a product from the table
# cursor.execute('DELETE FROM products WHERE id = 1003')

# Deletes the complete table from the database
# cursor.execute("DROP TABLE IF EXISTS products")
#4. Commit the changes and close the connection
conn.commit()
conn.close()


