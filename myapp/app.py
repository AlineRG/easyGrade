from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myDB.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#Routes 

@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and check_password_hash(user.password, login_form.password.data):
            flash('Inicio de sesion existoso')
            return redirect(url_for('index'))
        else:
            flash('Usuario o Contraseña incorrectos')

@app.route('/register', methods=['GET', 'POST'])
def register():
    login_form = LoginForm()
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        hashed_password = generate_password_hash(register_form.password.data, method = 'sha256')
        new_user = User(username = register_form.username.data, email = register_form.email.data, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registro exitoso')
        return redirect(url_for('login'))
    
    return render_template('login.html', login_form=login_form, register_form=register_form)


#Modelo de usuario
class User(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    email = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable=False)

#Formulario de registro
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=10, max=50)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)])
    submit = SubmitField('Sign Up')

#Formulario de inicio de sesion
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=10, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)])
    submit = SubmitField('Log In')

@app.route('/')
def index():
    return "Bienvenido a EasyGrade"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)