def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            preco FLOAT
        )
    """)
    conn.commit()

def inserir_produto(conn, nome, preco):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
    conn.commit()

def listar_produtos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco FROM produtos")
    resultados = cursor.fetchall()
    return [{'id': r[0], 'nome': r[1], 'preco': r[2]} for r in resultados]

