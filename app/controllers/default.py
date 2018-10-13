from app import app


@app.route("/index")
@app.route("/")
def index():
    return "Apresenta o index"


@app.route("/test/<int:id>")
def test(id):
    return "Teste"

@app.route("/test1/", methods=['GET'])
def test1():
    return "Teste1"
