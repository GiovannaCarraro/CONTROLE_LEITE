import mysql.connector

def criar_conexo():
    conexao = mysql.connector.connect(
                                    host= "localhost",
                                    port=3306,
                                    user="root",
                                    password="root",
                                    database="bd_controleleite"
                                     )
    
    cursor = conexao.cursor()

    return conexao, cursor

if __name__ == "__main__":
   conexao, cursor = criar_conexo()
   print(conexao)