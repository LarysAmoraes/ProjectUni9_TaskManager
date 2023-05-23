import sqlite3

# Conecta-se ao banco de dados (cria o arquivo caso não exista)
conn = sqlite3.connect('login_database.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria a tabela "users" para armazenar informações de login
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

# Salva as alterações e fecha a conexão
conn.commit()
conn.close()
