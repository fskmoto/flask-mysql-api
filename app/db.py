import MySQLdb
import os
import time

def conectar_db():
    while True:
        try:
            conexao = MySQLdb.connect(
                host=os.environ.get('DB_HOST', 'localhost'),
                user=os.environ.get('DB_USER', 'root'),
                passwd=os.environ.get('DB_PASSWORD', 'root'),
                db=os.environ.get('DB_NAME', 'produtosdb'),
                port=3306
            )
            return conexao
        except MySQLdb.Error:
            print("Aguardando banco de dados...")
            time.sleep(2)

