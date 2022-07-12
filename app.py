from flask import Flask, render_template, Response


app = Flask(__name__)


@app.route('/')
def index():
    return Response('<h1>Welcome to Flasker!</h1>')
