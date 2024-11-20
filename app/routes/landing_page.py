from flask import Blueprint
from flask import render_template

landing_page = Blueprint("landing_page", __name__)


@landing_page.route("/")
@landing_page.route("/index")
def index():
    return render_template("index.html")
