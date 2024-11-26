from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def primeira_pagina():
    return render_template('index.html')


