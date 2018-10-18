from flask import render_template
from app import app, db

from app.models.table import User
from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html', form=form)


@app.route("/test/<info>")
@app.route("/test/", defaults={"info": None})
def test(info):
    # ======= DELETE ======= #
    # d = User.query.filter_by(username="edupajeu").first()
    # db.session.delete(d)
    # db.session.commit()
    # ======= UPDATE ======= #
    # u = User.query.filter_by(username="edupajeu").first()
    # u.name = "Eduardo P."
    # db.session.add(u)
    # db.session.commit()
    # ======= QUERY ======== #
    q = User.query.filter_by(username="edupajeu").first()
    print(q.username, q.name)
    # ======= CREATE ======= #
    # i = User(username="edupajeu", password="12345", name=" Eduardo Pajeú", email="edupajeu@gmail")
    # db.session.add(i)
    # db.session.commit()
    return 'OK'


