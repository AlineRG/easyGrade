from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Email, Length
from wtforms.fields import DateField
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Contacto, db

edit_profile_page = Blueprint("edit_profile", __name__)


# Formulario de registro
class EditProfileForm(FlaskForm):
    nombre = StringField("Nombre", validators=[InputRequired(), Length(max=50)])
    apellido = StringField("Apellido", validators=[InputRequired(), Length(max=50)])
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=100)])
    telefono = StringField(
        "Telefono", validators=[InputRequired(), Length(min=5, max=50)]
    )
    direccion = StringField(
        "Direccion", validators=[InputRequired(), Email(), Length(max=50)]
    )
    cumpleanos = DateField("Fecha de Nacimiento", validators=[InputRequired()])
    rol = SelectField(
        "Rol",
        choices=[("estudiante", "Estudiante"), ("maestro", "Maestro")],
        validators=[InputRequired()],
    )
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

    return render_template("editProfile.html", edit_profile_form=edit_profile_form)
