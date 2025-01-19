import sqlite3
import os

def connect_db():
    return sqlite3.connect('module14\\План написания админ панели\\products.db')

def initiate_db():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            filename TEXT
        )
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute ('''
        SELECT * FROM Products
    ''')
    products = cursor.fetchall()
    connection.close()
    return products

def add_product(title, description, price):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute ('''
        INSERT INTO Products (title, description, price, filename)
        VALUES (?, ?, ?, ?)
    ''', (title, description, price))
    connection.commit()
    connection.close()

initiate_db()

def populate_products():
    products = [
        ('Помидоры', 'Свежие помидоры', 100, 'tomato'),
        ('Баклажаны', 'Свежие баклажаны', 120, 'eggplant'),
        ('Лук', 'Свежий лук', 80, 'onion'),
        ('Картофель', 'Свежий картофель', 90, 'potato')
    ]
    connection = connect_db()
    cursor = connection.cursor()
    cursor.executemany ('''
        INSERT INTO Products (title, description, price, filename)
        VALUES (?, ?, ?, ?)
    ''', products)
    connection.commit()
    connection.close()

populate_products()