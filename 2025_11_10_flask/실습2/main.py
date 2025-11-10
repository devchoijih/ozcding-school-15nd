from flask import Flask #Flask 가져오기
app = Flask(__name__)  # 내가 Flask를 쓸건데 app이라는 이름을 통해서 쓸거임

@app.route('/')
def home():
    return 'Home'

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/hello/kk')
def hello_kk():
    return 'Hello_kk'

@app.route('/user/<name>')
def greet(name):
    return f"{name}님 만나서 반갑습니다."

if __name__ == '__main__':
    app.run(debug=True)