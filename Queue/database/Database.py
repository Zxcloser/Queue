from sqlite3 import *


with connect('database.db') as db:
    cursor = db.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table2 (id INTEGER PRIMARY KEY,Freedom TEXT, FIO TEXT)""") #queue
    for i in range(0,16):
        cursor.execute('''SELECT * FROM table2 WHERE Freedom !=? or Freedom != ? ''', ("Свободно" , "Занято",))
        insert_inf = (i+1, "Свободно")
        query = """ INSERT INTO table2(id, Freedom) VALUES (?, ?)"""
        cursor.execute(query, insert_inf)


