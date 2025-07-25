
from flask import Flask, jsonify, request
from db import conectar_db
from models import criar_tabela, inserir_produto, listar_produtos

app = Flask(__name__)
conexao = conectar_db()
criar_tabela(conexao)

@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = listar_produtos(conexao)
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def add_produto():
    dados = request.get_json()
    nome = dados.get('nome')
    preco = dados.get('preco')
    if not nome or not preco:
        return jsonify({'erro': 'Campos nome e preco são obrigatórios'}), 400

    inserir_produto(conexao, nome, preco)
    return jsonify({'mensagem': 'Produto inserido com sucesso!'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

