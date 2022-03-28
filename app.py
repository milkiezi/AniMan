from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from blueprints.home import home
from blueprints.anime import anime
from blueprints.manga import manga
from blueprints.group import group
from blueprints.about import about
from blueprints.models import db, Student

app = Flask(__name__)

app.config['SECRET_KEY'] = 'app-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(home)
app.register_blueprint(anime)
app.register_blueprint(manga)
app.register_blueprint(group)
app.register_blueprint(about)