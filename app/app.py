from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/<path>')
def index(path=""):
    if path != "":
        return redirect(url_for('.index'))
    return render_template('index.html')




app.config.from_object("app.config")
app.config.from_pyfile("app.cfg", silent=True)
