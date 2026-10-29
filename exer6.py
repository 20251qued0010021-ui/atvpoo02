from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
carros_bd = []

@app.route("/carros", methods=["GET"])
def retornarcarros():
    return jsonify(carros_bd)

@app.route("/carros", methods=["POST"])
def salvarcarros():
    global id
    id = id + 1
    dados = request.get.json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("ano")
    carro = {"id": id, "modelo": id, "marca": marca, "ano": ano}
    carros_bd.append
    return jsonify(carro) 

@app.route("/carros/<int:id>", methods=["PUT"])
def editarcarros(id):
    dados = request.get.json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("")
    for carro in carros_bd:
        if carro["id"] == id:
            carro["ano"] == ano
            carro["marca"] == marca
            return jsonify(carro), 200

    return jsonify({"erro": "carro não encontrado"}), 404

@app.route("/carros/<int:id>", methods=["DELETE"])
def removercarros(id):
    for carro in carros_bd:
        if carro["id"] == id:
            carros_bd.remove(carro)
        return "", 204

    return jsonify({"erro": "carro não encontrado"}), 404

app.run(debug=True)