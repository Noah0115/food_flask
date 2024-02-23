# user_view.py
from flask import Blueprint
from app.controller import user_controller

user_blueprint = Blueprint('user', __name__)
user_blueprint.route('/register', methods=['GET', 'POST'])(user_controller.register)
user_blueprint.route('/login', methods=['GET', 'POST'])(user_controller.login)
user_blueprint.route('/logout', methods=['GET','POST'])(user_controller.logout)
user_blueprint.route('/profile', methods=['GET', 'POST'])(user_controller.profile)
user_blueprint.route('/get_csrf', methods=['GET', 'POST'])(user_controller.get_csrf)
user_blueprint.route('/check_current_login', methods=['GET','POST'])(user_controller.check_current_login)
