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

    def cadastros_contatos(self, nome, telefone, email, categoria):
        self.cursor.execute("""
        INSERT INTO Contatos (nome, telefone, email, categoria)
        VALUES(?, ?, ?, ?)          
        """, (nome, telefone, email, categoria))

        self.conectar.commit()

    def listar_contatos(self):
        self.cursor.execute("SELECT * FROM Contatos")

        dados = self.cursor.fetchall()

        return dados 