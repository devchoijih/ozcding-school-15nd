from flask import Flask, render_template  # Flask 가져오기
app = Flask(__name__)  # 내가 Flask를 쓸건데 app이라는 이름을 통해서 쓸거임

@app.route('/hello')
def home():
    return render_template("hello.html", name="BE15")

@app.route('/user/<username>')
def user_name(username):
    return render_template("user.html", username=username)

@app.route('/fruits')
def friuts():

    fruits = ["apple", "banana", "orange"]
    return render_template("fruits.html", fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True)