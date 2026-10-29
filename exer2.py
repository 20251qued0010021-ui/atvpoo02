from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
alunos = []

@app.route("/alunos", methods=["GET"])
def retornarAlunos():
    return jsonify(alunos)

@app.route("/alunos", methods=["POST"])
def salvarAlunos():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    idade = dados.get("idade")
    curso = dados.get("curso")
    filme = {"id": id, "nome": nome, "idade": idade, "curso": curso}
    alunos.append
    return jsonify(alunos) 

@app.route("/alunos/<int:id>", methods=["PUT"])
def editarAlunos(id):
    dados = request.get.json()
    nome = dados.get("nome")
    idade = dados.get("idade")
    curso = dados.get("curso")
    for aluno in alunos:
        if aluno["id"] == id:
            aluno["idade"] == idade
            aluno["curso"] == curso
            return jsonify(alunos), 200

    return jsonify({"erro": "Aluno não encontrado"}), 404

@app.route("/alunos/<int:id>", methods=["DELETE"])
def removerAlunos(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
        return "", 204

    return jsonify({"erro": "Aluno não encontrado"}), 404

app.run(debug=True)