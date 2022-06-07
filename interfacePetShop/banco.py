import sqlite3
from sqlite3 import Error
nomeBanco = "petshop.db"

def ConexaoBanco():
    conexao =nomeBanco
    try:
        conexao = sqlite3.connect(nomeBanco)
    except Error as erro:
        print(erro)
    return conexao


def pesquisa(query):
    vcon = ConexaoBanco()
    c = vcon.cursor()
    c.execute(query)
    resposta = c.fetchall()
    vcon.close()
    return resposta


def alterar(query):
    try:
        vcon = ConexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as erro:
        print(erro)