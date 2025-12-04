import sqlite3
import os

DB_NAME = "coursemax.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            cpf TEXT,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS disciplinas (
            id INTEGER PRIMARY KEY,
            id_usuario INTEGER,
            nome TEXT NOT NULL,
            color TEXT,
            horas INTEGER,
            presencas INTEGER,
            faltas INTEGER,
            modulos TEXT, 
            provas TEXT,
            FOREIGN KEY(id_usuario) REFERENCES users(id)
        )
    ''')
    
    conn.commit()
    conn.close()

init_db()