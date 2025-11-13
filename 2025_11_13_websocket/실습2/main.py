from flask import Flask
from flask_sock import Sock
import threading
import time

app = Flask(__name__)
sock = Sock(app)

connections = set()

@sock.route('/ws')
def websocket(ws):
    while True:
        connections.add(ws)
        data = ws.receive()
        if data is None:
            break

def background_job():
    while True:
        time.sleep(5)
        for ws in list(connections):
            try:
                ws.send("서버가 클라이언트에게 알림 보냄")
            except Exception:
                connections.discard(ws)
                pass


threading.Thread(target=background_job, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)