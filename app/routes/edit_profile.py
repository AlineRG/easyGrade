from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, db

edit_profile_page = Blueprint("edit_profile", __name__)


# Formulario de registro
class RegisterForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=5, max=50)]
    )
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])
    password = PasswordField(
        "Password", validators=[InputRequired(), Length(min=8, max=20)]
    )
    submit = SubmitField("Sign Up")


# Formulario de inicio de sesion
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])
    password = PasswordField(
        "Password", validators=[InputRequired(), Length(min=8, max=20)]
    )
    submit = SubmitField("Log In")


@edit_profile_page.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    login_form = LoginForm()
    register_form = RegisterForm()

    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = User.query.filter_by(email=login_form.email.data).first()
        if user and check_password_hash(user.password, login_form.password.data):
            flash("Inicio de sesion exitoso")
            return redirect(url_for("home_page.homePage"))
        else:
            flash("Usuario o Contraseña incorrectos")

    return render_template(
        "editProfile.html", login_form=login_form, register_form=register_form
    )


