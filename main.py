import sqlite3  # Importa o módulo sqlite3, que fornece a API do Python para trabalhar com bancos SQLite.
from pathlib import Path  # Importa a classe Path, que facilita a manipulação de caminhos de arquivos e pastas.

ROOT_DIR = Path(__file__).parent  # __file__ representa o caminho do arquivo atual (este script). 
# .parent pega a pasta que contém esse arquivo, ou seja, a pasta raiz do projeto.
# Exemplo: se o arquivo estiver em /projeto/main.py, então Path(__file__).parent será /projeto.
DB_NAME = 'db.sqlite3'  # Define o nome do arquivo do banco de dados SQLite que será usado.
DB_FILE = ROOT_DIR / DB_NAME  # Cria o caminho completo do banco usando a pasta raiz + nome do arquivo.
# Em outras palavras, DB_FILE vira algo como /projeto/db.sqlite3.

con = sqlite3.connect(DB_FILE)  # Abre a conexão com o banco de dados SQLite.
# Se o arquivo db.sqlite3 não existir, o SQLite cria automaticamente.
# A variável con representa a conexão ativa com o banco.
cursor = con.cursor()  # Cria um cursor, que serve para executar comandos SQL no banco.
# O cursor é o objeto que envia instruções como SELECT, INSERT, UPDATE e DELETE.

#SQL  # Espaço reservado para escrever os comandos SQL do projeto.
# Aqui você pode colocar instruções como CREATE TABLE, INSERT INTO, SELECT, etc.
# Exemplo: cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")

con.close()  # Fecha a conexão com o banco de dados para liberar recursos do sistema.
# Isso é importante para encerrar corretamente a comunicação com o arquivo SQLite.
cursor.close()  # Fecha o cursor, finalizando o objeto usado para executar instruções SQL.
# Depois disso, o código não pode mais executar comandos SQL com esse cursor.