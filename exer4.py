from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
funcionarios_bd = []

@app.route("/funcionarios", methods=["GET"])
def retornarFuncionarios():
    return jsonify(funcionarios_bd), 200

@app.route("/funcionarios", methods=["POST"])
def salvarFuncionario():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    cargo = dados.get("cargo")
    salario = dados.get("salario")
    
    id = id + 1
    
    funcionario = {
        "id": id,
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }
    
    funcionarios_bd.append(funcionario)
    
    return jsonify(funcionario), 201

@app.route("/funcionarios/<int:id>", methods=["PUT"])
def editarFuncionario(id):
    dados = request.get_json()
    
    for funcionario in funcionarios_bd:
        if funcionario["id"] == id:
            funcionario["nome"] = dados.get("nome", funcionario["nome"])
            funcionario["cargo"] = dados.get("cargo", funcionario["cargo"])
            funcionario["salario"] = dados.get("salario", funcionario["salario"])
            return jsonify(funcionario), 200

    return jsonify({"erro": "Funcionário não encontrado"}), 404

@app.route("/funcionarios/<int:id>", methods=["DELETE"])
def removerFuncionario(id):
    for funcionario in funcionarios_bd:
        if funcionario["id"] == id:
            funcionarios_bd.remove(funcionario)
            return "", 204 

    return jsonify({"erro": "Funcionário não encontrado"}), 404

app.run(debug=True)