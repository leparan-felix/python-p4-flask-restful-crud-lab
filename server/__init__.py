# from flask import Flask
# from .extension import db
# from .models import Plant  # ✅ Make sure this comes after db

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.init_app(app)

#     return app
