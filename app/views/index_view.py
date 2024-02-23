# encoding:utf-8
from flask import Blueprint
from app.controller import index_controller
from flask_login import login_required, current_user

index_blueprint = Blueprint('index', __name__)
index_blueprint.route('/index', methods=['GET','POST'])(index_controller.index)
index_blueprint.route('/index/get_food_index', methods=['GET','POST'])(index_controller.get_food_index)
index_blueprint.route('/index/food_search', methods=['GET','POST'])(index_controller.food_search)
index_blueprint.route('/index/data_anl_bar', methods=['GET','POST'])(index_controller.data_anl_bar)
index_blueprint.route('/index/data_anl_pie', methods=['GET','POST'])(index_controller.data_anl_pie)
index_blueprint.route('/index/data_anl_pie_flavour', methods=['GET','POST'])(index_controller.data_anl_pie_flavour)
index_blueprint.route('/index/data_rader', methods=['GET','POST'])(index_controller.data_rader)
