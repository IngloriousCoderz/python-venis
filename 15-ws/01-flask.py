from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


# 2 + "2"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route("/ultimate_question/<int:answer>")
def fundamental_question(answer):
    return f"The Answer to the ultimate question of Life, the Universe, and Everything, is {answer}"


@app.route("/three/<path:subpath>")
def three(subpath):
    return f"Three {' '.join(escape(subpath).split('/'))}"


@app.route("/projects/")
def projects():
    return "The projects page"


@app.route("/about")
def about():
    return "The about page"


@app.route("/hello")
@app.route("/hello/<name>")
def say_hello(name="world"):
    return render_template('hello.html', who=escape(name))
