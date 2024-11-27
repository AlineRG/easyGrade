from flask import Flask
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mysecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///easyGrade.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import home_page, landing_page, login_register

    app.register_blueprint(landing_page.landing_page)
    app.register_blueprint(login_register.login_register, url_prefix="/auth")
    app.register_blueprint(home_page.home_page)

    with app.app_context():
        db.create_all()

    return app
