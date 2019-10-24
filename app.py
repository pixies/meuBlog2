from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CadastroUsuarioForm

#from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meublog.db'
app.config['SECRET_KEY'] = '1c9d3bdf0d6ce70779737468b6f8d71e'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = CadastroUsuarioForm()
    
    return render_template('register.html', form=form)















"""
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

"""


if __name__ == '__main__':
    app.run(debug=True)