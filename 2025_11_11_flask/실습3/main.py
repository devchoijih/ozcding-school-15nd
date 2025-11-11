from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return jsonify({"message": f"{name}님 환영합니다"})

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route("/user/<name>")
# def user(name):
#     return {"message": f"{name}님 환영합니다"}
#
# if __name__ == "__main__":
#     app.run(debug=True)
