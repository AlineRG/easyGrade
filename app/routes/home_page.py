from flask import Blueprint, render_template

home_page = Blueprint("home_page", __name__)


@home_page.route("/homePage")
def homePage():
    return render_template("homePage.html")
