import sqlite3 
conn = sqlite3.connect("tareas.db") 
cursor = conn.cursor() 
cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios ( id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT UNIQUE NOT NULL, contraseña TEXT NOT NULL ) """) 
cursor.execute(""" CREATE TABLE IF NOT EXISTS tareas ( id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT NOT NULL, descripcion TEXT NOT NULL ) """) 
conn.commit() 
conn.close() 
print("Base de datos creada: tareas.db")
