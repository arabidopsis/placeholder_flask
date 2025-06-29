from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/<path>')
def index(path=""):
    if path != "":
        return redirect(url_for('.index'))
    return render_template('index.html')




app.config.from_object("placeholder_flask.config")
app.config.from_pyfile("placeholder-flask.cfg", silent=True)
