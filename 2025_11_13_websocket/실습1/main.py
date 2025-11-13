from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@sock.route('/ws')
def websocket(ws):
    while True:
        data = ws.receive()
        if data is None:
            break
        ws.send(f"서버가 이 메세지 받음 : {data}")

if __name__ == "__main__":
    app.run(debug=True)