from flask import  render_template
from app import app


@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html', user=user
                           )


@app.route("/test/<int:id>")
def test(id):
    return "Teste"

@app.route("/test1/", methods=['GET'])
def test1():
    return "Teste1"
