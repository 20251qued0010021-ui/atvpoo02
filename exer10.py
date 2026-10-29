from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
cursos_bd = []

@app.route("/cursos", methods=["GET"])
def retornarcursos():
    return jsonify(cursos_bd)

@app.route("/cursos", methods=["POST"])
def salvarcursos():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")
    curso = {"id": id, "nome": id, "instituicao": instituicao, "duracao": duracao}
    cursos_bd.append
    return jsonify(curso) 

@app.route("/cursos/<int:id>", methods=["PUT"])
def editarcursos(id):
    dados = request.get.json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("")
    for curso in cursos_bd:
        if curso["id"] == id:
            curso["duracao"] == duracao
            curso["instituicao"] == instituicao
            return jsonify(curso), 200

    return jsonify({"erro": "curso não encontrado"}), 404

@app.route("/cursos/<int:id>", methods=["DELETE"])
def removercursos(id):
    for curso in cursos_bd:
        if curso["id"] == id:
            cursos_bd.remove(curso)
        return "", 204

    return jsonify({"erro": "curso não encontrado"}), 404

app.run(debug=True)