from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
musicas_bd = []

@app.route("/musicas", methods=["GET"])
def retornarmusicas():
    return jsonify(musicas_bd)

@app.route("/musicas", methods=["POST"])
def salvarmusicas():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    artista = dados.get("artista")
    ano = dados.get("ano")
    musica = {"id": id, "nome": id, "artista": artista, "ano": ano}
    musicas_bd.append
    return jsonify(musica) 

@app.route("/musicas/<int:id>", methods=["PUT"])
def editarmusicas(id):
    dados = request.get.json()
    nome = dados.get("nome")
    artista = dados.get("artista")
    ano = dados.get("")
    for musica in musicas_bd:
        if musica["id"] == id:
            musica["ano"] == ano
            musica["artista"] == artista
            return jsonify(musica), 200

    return jsonify({"erro": "musica não encontrado"}), 404

@app.route("/musicas/<int:id>", methods=["DELETE"])
def removermusicas(id):
    for musica in musicas_bd:
        if musica["id"] == id:
            musicas_bd.remove(musica)
        return "", 204

    return jsonify({"erro": "musica não encontrado"}), 404

app.run(debug=True)