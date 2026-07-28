import sqlite3

def connect_db():
    return sqlite3.connect('store.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_product(name, price, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, price, quantity)
        VALUES (?, ?, ?)
    ''', (name, price, quantity))
    conn.commit()
    conn.close()

def read_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_product(id, price):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products
        SET price = ?
        WHERE id = ?
    ''', (price, id))
    conn.commit()
    conn.close()

def delete_product(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()

    create_product("Телефон", 50000.0, 10)
    create_product("Наушники", 5000.0, 25)

    print(read_products())
