import sqlite3


NAME_DATABASE = "dev_base.db"
conn = sqlite3.connect(NAME_DATABASE)
cursor = conn.cursor()


def close_connect():
    conn.commit()
    cursor.close()
    conn.commit()


def init_base():
    try:
        cursor.execute("""CREATE TABLE clientes(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name varchar(255), 
                        cpf varchar(255),
                        cep varchar(255),
                        adress varchar(255));""")
    except:
        pass
    close_connect()


def cadastrar_dados(data):
    cursor.execute("""
                   insert into clientes (name,cpf,cep,adress)
                   values(?,?,?,?)
                   """, data)
    close_connect()
    
    

