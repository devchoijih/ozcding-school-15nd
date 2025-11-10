from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
            <form method="get" action="/greet">
                <input type="text" name="name" placeholder="이름 입력" required>
                <button type="submit">인사하기</button>
            </form>
        """

@app.route("/greet", methods=["GET"])
def greet():
    return render_template("greet.html", name=request.args.get("name"))

if __name__ == '__main__':
    app.run(debug=True)