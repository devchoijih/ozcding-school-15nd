from flask import Flask, request, jsonify

app = Flask(__name__)

todos = {
    1 : "밥먹기",
    2 : "놀기"
}

# Read : 전체 목록 조회
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# Read : 특정 목록 조회
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    task = todos.get(todo_id)

    if not task:
        return jsonify({"error": "그런건 없어요"}), 404

    return jsonify({ todo_id : task })

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    new_id = max(todos.keys()) + 1 if todos else 1
    todos[new_id] = data["task"]

    return jsonify({ new_id : data["task"] }), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error":"못찾음"}, 404)

    data = request.get_json()
    todos[todo_id] = data["task"]

    return jsonify({ todo_id : data["task"] })

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todos.pop(todo_id)
    return jsonify({}), 204

if __name__ == "__main__":
    app.run(debug=True)