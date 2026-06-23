import sqlite3

class Agenda:
    def __init__(self):
        self.conectar = sqlite3.connect('dados/agenda.db')
        #LEMBRAR: connect() -> cria uma conexão com o banco de dados.
        self.cursor = self.conectar.cursor()
         #LEMBRAR: cursor() -> cria um cursor, que é o objeto responsável por executar comandos SQL e acessar os resultados.
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
        #LEMBRAR: execute() -> método do cursor usado para executar um comando SQL no banco de dados SQLite
        dados = self.cursor.fetchall() 
        #LEMBRAR: fetchall() -> método usado para buscar todas as linhas retornadas por uma consulta SQL
        return dados 
    
    def buscar_contatos(self, buscar): 
        self.cursor.execute("SELECT * FROM Contatos WHERE nome = ? OR telefone = ? OR email = ?", (buscar, buscar, buscar))
        
        dados = self.cursor.fetchall() 
        
        return dados
    
    def buscar_por_id(self, id):
        self.cursor.execute("SELECT * FROM Contatos WHERE id = ?", (id,))
        return self.cursor.fetchone() #LEMBRAR: .fetchone() -> retorna só uma tupla, uma linha por vez
    
    def editar_contato(self, id, nome, telefone, email, categoria): #Usando ID pois é a forma mais segura de busca já que ele é PK
        self.cursor.execute("UPDATE Contatos SET nome = ?, telefone = ?, email = ?, categoria = ? WHERE id = ?", (nome, telefone, email, categoria, id))

        self.conectar.commit()

    def remover_contato(self, id):
        self.cursor.execute("DELETE FROM Contatos WHERE id = ?", (id,))

        self.conectar.commit()