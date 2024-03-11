from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/<path>')
def index(path=''):
    return render_template('index.html')




app.config.from_object("app.config")
app.config.from_pyfile("app.cfg", silent=True)
