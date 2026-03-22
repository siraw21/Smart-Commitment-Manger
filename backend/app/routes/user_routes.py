from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import User

user_bp = Blueprint("user_bp", __name__)

# Create user
@user_bp.route('/users', methods=['POST'])
def create_user():
   data = request.get_json()

   new_user = User(
      name = data['name'],
      email = data['email'],
      password = data['password']
   )

   db.session.add(new_user)
   db.session.commit()

   return jsonify({"message": "User created"}), 201

# Get All Users
@user_bp.route('/users', methods=['GET'])
def get_users():
   users = User.query.all()

   result = []

   for user in users:
      result.append({
         "id": user.id,
         "name": user.name,
         "email": user.email
      })

   return jsonify(result)