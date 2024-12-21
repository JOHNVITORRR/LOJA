from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template("index.html")

@app.route('/produto')
def segunda_pagina():
    return render_template("produto.html")

@app.route('//carinho')
def terceira_pagina():
    return render_template("carrinho.html")



