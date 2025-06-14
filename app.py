from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/')
def index():
    if 'logged_in' in session:
        # Exemplo de jogos com probabilidades simuladas
        jogos = [
            {"time_casa": "Flamengo", "time_fora": "Palmeiras", "mercado": "1X2", "palpite": "1", "prob": 78},
            {"time_casa": "Santos", "time_fora": "Corinthians", "mercado": "Ambos Marcam", "palpite": "Sim", "prob": 72},
            {"time_casa": "Grêmio", "time_fora": "Internacional", "mercado": "Over 2.5", "palpite": "Mais", "prob": 75},
        ]
        return render_template("dashboard.html", jogos=jogos)
    return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['email'] == 'cledersonsilva388@gmail.com' and request.form['senha'] == '@Clederson123':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return "Login inválido"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)