from flask import Flask
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from app.extensions import db, migrate
from app.routes.user_routes import user_bp
from app.routes.task_routes import task_bp


# Create Database Instance
# db = SQLAlchemy()

# Create Migrate instance
# migrate = Migrate()

def create_app():
   app = Flask(__name__)

   app.config.from_object("app.config.Config")
   
   CORS(app)
   
   # Initialize database
   db.init_app(app)

   # Initialize Migrate
   migrate.init_app(app, db)

   # Register models
   from app.models import User

   # Register blueprint
   app.register_blueprint(user_bp)
   app.register_blueprint(task_bp)

   @app.route('/')
   def home():
      return {"message": "Backend with DB is running "}
   
   return app