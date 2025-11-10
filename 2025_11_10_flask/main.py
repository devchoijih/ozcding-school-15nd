from flask import Flask #Flask 가져오기
app = Flask(__name__)  # 내가 Flask를 쓸건데 app이라는 이름을 통해서 쓸거임

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)