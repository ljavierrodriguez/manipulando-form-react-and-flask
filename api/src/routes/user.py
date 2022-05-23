from flask import Blueprint, request, jsonify
from models import User
import cloudinary
import cloudinary.uploader

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():

    name = request.form['name']
    email = request.form['email']
    avatar = request.files['avatar']


    resp = cloudinary.uploader.upload(avatar, folder="avatarsapp")

    if not resp: return jsonify({ "msg": "Error al subir imagen"})
    
    user = User()
    user.name = name
    user.email = email
    user.avatar = resp["secure_url"]
    user.save()

    '''
    print(request.form)
    print(request.files)
    '''

    return jsonify(user.serialize())


@api.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users)