from flask import Flask
from app.models import db
from app.routes import home_page, landing_page, login_register, edit_profile
import app.modules


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mysecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///easyGrade.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(landing_page.landing_page)
    app.register_blueprint(login_register.login_register, url_prefix="/auth")
    app.register_blueprint(home_page.home_page)
    app.register_blueprint(edit_profile.edit_profile_page)

    with app.app_context():
        db.create_all()

    return app
