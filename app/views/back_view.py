# encoding:utf-8
from flask import Blueprint
from app.controller import back_user_controller, back_news_controller, back_food_controller

back_blueprint = Blueprint('back', __name__)
back_blueprint.route('/back/get_all_user', methods=['GET', 'POST'])(back_user_controller.get_all_user)
back_blueprint.route('/back/search_user', methods=['GET', 'POST'])(back_user_controller.search_user)
back_blueprint.route('/back/update_user', methods=['GET', 'POST'])(back_user_controller.update_user)
back_blueprint.route('/back/add_user', methods=['GET', 'POST'])(back_user_controller.add_user)
back_blueprint.route('/back/get_all_news', methods=['GET', 'POST'])(back_news_controller.get_all_news)
back_blueprint.route('/back/get_all_news_admin', methods=['GET', 'POST'])(back_news_controller.get_all_news_admin)
back_blueprint.route('/back/add_news', methods=['GET', 'POST'])(back_news_controller.add_news)
back_blueprint.route('/back/update_news', methods=['GET', 'POST'])(back_news_controller.update_news)
back_blueprint.route('/back/get_all_food', methods=['GET', 'POST'])(back_food_controller.get_all_food)
back_blueprint.route('/back/update_food', methods=['GET', 'POST'])(back_food_controller.update_food)
back_blueprint.route('/back/add_food', methods=['GET', 'POST'])(back_food_controller.add_food)
back_blueprint.route('/back/data_init', methods=['GET', 'POST'])(back_food_controller.data_init)
