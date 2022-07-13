import imp
from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

#DEFINING THE APP FUNCTION 
def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)


    migrate = Migrate()

    db.init_app(app)
    migrate.init_app(app, db)

    from app.blueprints.main import bp
    app.register_blueprint(bp)
    return app