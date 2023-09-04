#__init__ file turn folder into python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def build():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    ##Initialize database and passing it the app
    db.init_app(app)
    
    ## registering blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,File,Note

    with app.app_context():
        db.create_all()

    #build_database(app)

    return app

# ## Checking if database exist, if it does, don't overwrite
# def build_database(app):
    
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print("DATABASE")

## HTTP requests (POST,GET)
