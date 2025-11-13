from flask import Flask, render_template, request, session, redirect
from datetime import timedelta
from psutil import users

app = Flask(__name__)

app.secret_key = 'flask-secret-key' # 실제로 배포시에는 .env or yaml
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

#admin user
users = {
    'admin': 'admin',
    'user': 'user'
}

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['username'] = username

        return redirect('/secret')
    else:
        return redirect('/')

@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)