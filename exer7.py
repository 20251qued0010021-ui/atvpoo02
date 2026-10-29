from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
cidades_bd = []

@app.route("/cidades", methods=["GET"])
def retornarcidades():
    return jsonify(cidades_bd)

@app.route("/cidades", methods=["POST"])
def salvarcidades():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    cidade = {"id": id, "nome": id, "preco": preco, "categoria": categoria}
    cidades_bd.append
    return jsonify(cidade) 

@app.route("/cidades/<int:id>", methods=["PUT"])
def editarcidades(id):
    dados = request.get.json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("")
    for cidade in cidades_bd:
        if cidade["id"] == id:
            cidade["categoria"] == categoria
            cidade["preco"] == preco
            return jsonify(cidade), 200

    return jsonify({"erro": "cidade não encontrado"}), 404

@app.route("/cidades/<int:id>", methods=["DELETE"])
def removercidades(id):
    for cidade in cidades_bd:
        if cidade["id"] == id:
            cidades_bd.remove(cidade)
        return "", 204

    return jsonify({"erro": "cidade não encontrado"}), 404

app.run(debug=True)