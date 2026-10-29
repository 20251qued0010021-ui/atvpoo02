from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
produtos_bd = []

@app.route("/produtos", methods=["GET"])
def retornarprodutos():
    return jsonify(produtos_bd)

@app.route("/produtos", methods=["POST"])
def salvarprodutos():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    produto = {"id": id, "nome": id, "preco": preco, "categoria": categoria}
    produtos_bd.append
    return jsonify(produto) 

@app.route("/produtos/<int:id>", methods=["PUT"])
def editarprodutos(id):
    dados = request.get.json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("")
    for produto in produtos_bd:
        if produto["id"] == id:
            produto["categoria"] == categoria
            produto["preco"] == preco
            return jsonify(produto), 200

    return jsonify({"erro": "produto não encontrado"}), 404

@app.route("/produtos/<int:id>", methods=["DELETE"])
def removerprodutos(id):
    for produto in produtos_bd:
        if produto["id"] == id:
            produtos_bd.remove(produto)
        return "", 204

    return jsonify({"erro": "produto não encontrado"}), 404

app.run(debug=True)