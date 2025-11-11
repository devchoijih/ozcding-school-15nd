from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/hello")
def user():
    """
    Hello API
    ---
    responses:
        200:
         description: 성공 응답
         schema:
           type: object
           properties:
             message:
                type: string
                example: "Hello, OZ!"
    """

    return jsonify({"message": "Hello, OZ!"})

if __name__ == "__main__":
    app.run(debug=True)