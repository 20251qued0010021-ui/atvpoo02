from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
jogos_bd = []

@app.route("/jogos", methods=["GET"])
def retornarjogos():
    return jsonify(jogos_bd)

@app.route("/jogos", methods=["POST"])
def salvarjogos():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")
    jogo = {"id": id, "nome": id, "genero": genero, "ano": ano}
    jogos_bd.append
    return jsonify(jogo) 

@app.route("/jogos/<int:id>", methods=["PUT"])
def editarjogos(id):
    dados = request.get.json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("")
    for jogo in jogos_bd:
        if jogo["id"] == id:
            jogo["ano"] == ano
            jogo["genero"] == genero
            return jsonify(jogo), 200

    return jsonify({"erro": "jogo não encontrado"}), 404

@app.route("/jogos/<int:id>", methods=["DELETE"])
def removerjogos(id):
    for jogo in jogos_bd:
        if jogo["id"] == id:
            jogos_bd.remove(jogo)
        return "", 204

    return jsonify({"erro": "jogo não encontrado"}), 404

app.run(debug=True)