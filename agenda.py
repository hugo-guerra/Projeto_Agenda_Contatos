import sqlite3

class Agenda:
    def __init__(self):
        self.conectar = sqlite3.connect('dados/agenda.db')
        self.cursor = self.conectar.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone INT,
            email TEXT UNIQUE,
            categoria TEXT
        )
        """)

        self.conectar.commit()