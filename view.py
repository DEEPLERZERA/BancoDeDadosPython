import sqlite3 as lite
from datetime import datetime

con = lite.connect('dados.db')

#Inserir inventário

def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario (nome, local, descricao, modelo, data_da_compra, valor_da_compra, serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

#Deletar item

def deletar_form(i):
    cur = con.cursor()
    query = "DELETE FROM inventario WHERE id = ?"
    cur.execute(query, i)



#Atualizar inventário
def atualizar_form(i):
    cur = con.cursor()
    query = "UPDATE inventario SET nome = ?, local = ?, descricao = ?, modelo = ?, data_da_compra = ?, valor_da_compra = ?, serie = ?, imagem = ? WHERE id = ?"
    cur.execute(query, i)



#Ver inventário
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM inventario")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
        return lista_itens 


#Ver item 
def ver_item(i):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM inventario WHERE id = ?", i)
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
        return lista_itens


