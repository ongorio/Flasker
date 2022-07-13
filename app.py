from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime

from utils.secrets import get_secrets

app = Flask(__name__)


# App Configuration
secrets = get_secrets('env.json')

app.config['SECRET_KEY'] = secrets['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{secrets["DB"]["USERNAME"]}:{secrets["DB"]["PASSWORD"]}@{secrets["DB"]["HOST"]}/{secrets["DB"]["NAME"]}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# DB Configuration
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.today)

    def __repr__(self):
        return f'<Post> {self.title}'


@app.route('/')
def index():
    posts = Post.query.all().order_by(Post.pub_date)

    return render_template('index.html', posts=posts)


# Posts Views




# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def permission_denied(e):
    return render_template('errors/403.html'), 403


@app.errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500
