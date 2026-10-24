import sqlite3
from typing import Any

from schema.models import ProductCreate, ProductUpdate

class Database:

    #Initialize the database 
    def __init__(self):
        self.conn = sqlite3.connect('products.db',check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    #Create a table to store product data
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY ,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )''')
        self.conn.commit()

    def create(self, product:ProductCreate):
        #find the next id 

        self.cursor.execute('SELECT MAX(id) FROM products')
        result = self.cursor.fetchone()
        new_id = int(result[0])+1 if None not in result else 1

        # self.cursor.execute('''
        #     INSERT INTO products (id, name, price, stock) VALUES
        #         (?,?,?,?)''', (new_id, product.name, product.price,product.stock))

        self.cursor.execute('''
            INSERT INTO products (id, name, price, stock) VALUES
                 (:id,:name,:price,:stock)''',{
                     "id":new_id,
                     **product.model_dump()

                 })

        self.conn.commit()
        return new_id

    def get(self, id: int) -> dict[str, Any] | None:
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (id,))
        row = self.cursor.fetchone()          # a tuple, or None
        # tuple -> dict (order = table definition)
        return {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "stock": row[3],
        } if row else None

    def upadte(self, id :int, product_update:ProductUpdate):

        data = product_update.model_dump(exclude_none=True)
        set_clause = ", ".join(f"{key} = :{key}" for key in data.keys())

        self.cursor.execute('''
            UPDATE products SET '''+ set_clause +''' WHERE id = :id''',
            {
                "id":id,
                **data
            })
        self.conn.commit()
        return self.get(id)

    def delete(self, id:int):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        
        self.conn.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.conn.close()   