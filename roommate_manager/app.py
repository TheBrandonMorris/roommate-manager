from pathlib import Path

from flask import Flask
import json

app = Flask(__name__)
path = Path('db.json')
db = json.loads(path.read_text())
x = db['Users']


@app.route('/')
def index():
    return render_template_with_Users("index.html")


@app.route('/profile/<user>')
def profile(user):
    return render_template_with_Users("user.html", user=user)


@app.route('/bills/')
def bills():
    return render_template_with_Users("bills.html")


def render_template_with_Users(template, **kwargs):
    return render_template(template, Users=x, **kwargs)

