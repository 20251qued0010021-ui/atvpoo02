from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
restaurantes_bd = []

@app.route("/restaurantes", methods=["GET"])
def retornarrestaurantes():
    return jsonify(restaurantes_bd)

@app.route("/restaurantes", methods=["POST"])
def salvarrestaurantes():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade = dados.get("cidade")
    restaurante = {"id": id, "nome": id, "tipo": tipo, "cidade": cidade}
    restaurantes_bd.append
    return jsonify(restaurante) 

@app.route("/restaurantes/<int:id>", methods=["PUT"])
def editarrestaurantes(id):
    dados = request.get.json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade = dados.get("")
    for restaurante in restaurantes_bd:
        if restaurante["id"] == id:
            restaurante["cidade"] == cidade
            restaurante["tipo"] == tipo
            return jsonify(restaurante), 200

    return jsonify({"erro": "restaurante não encontrado"}), 404

@app.route("/restaurantes/<int:id>", methods=["DELETE"])
def removerrestaurantes(id):
    for restaurante in restaurantes_bd:
        if restaurante["id"] == id:
            restaurantes_bd.remove(restaurante)
        return "", 204

    return jsonify({"erro": "restaurante não encontrado"}), 404

app.run(debug=True)