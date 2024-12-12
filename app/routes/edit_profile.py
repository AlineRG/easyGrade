from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Contacto, db

edit_profile_page = Blueprint("edit_profile", __name__)


# Formulario de registro
class EditProfileForm(FlaskForm):
    telefono = StringField(
        "Telefono", validators=[InputRequired(), Length(min=5, max=50)]
    )
    direccion = StringField("Direccion", validators=[InputRequired(), Email(), Length(max=50)])
    submit = SubmitField("Guardar")



@edit_profile_page.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    edit_profile_form = EditProfileForm()

    # if edit_profile_form.validate_on_submit():
    #     email = edit_profile_form.email.data
    #     password = edit_profile_form.password.data

    #     user = User.query.filter_by(email=edit_profile_form.email.data).first()
    #     if user and check_password_hash(user.password, edit_profile_form.password.data):
    #         flash("Inicio de sesion exitoso")
    #         return redirect(url_for("home_page.homePage"))
    #     else:
    #         flash("Usuario o Contraseña incorrectos")

    return render_template(
        "editProfile.html", edit_profile_form=edit_profile_form
    )


