# encoding:utf-8
from flask import Blueprint
from flask_login import login_required, current_user
from app.controller import index_controller, goods_controller

goods_blueprint = Blueprint('goods', __name__)
goods_blueprint.route('/goods', methods=['GET','POST'])(goods_controller.goods)
goods_blueprint.route('/goods/alltypes', methods=['GET','POST'])(goods_controller.goods_type)
goods_blueprint.route('/goods/goods_search_by_type', methods=['GET','POST'])(goods_controller.goods_search_by_type)
goods_blueprint.route('/goods/goods_info', methods=['GET','POST'])(goods_controller.goods_info)
goods_blueprint.route('/goods/search_goods', methods=['GET','POST'])(goods_controller.search_goods)
