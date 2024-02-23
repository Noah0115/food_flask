# encoding:utf-8
from sqlalchemy import *
from flask import jsonify, request
from urllib.parse import quote
from app.config import STATIC_PREIFX
from app.model.Data import Data, DataSchema,Data_Single_Schema
from app.model.Types import Types, TypesSchema
from app.utils.message import *
from app.utils.url_parse import *

data_schema = DataSchema(many=True)
single_data_schema = Data_Single_Schema(many=True)
type_schema = TypesSchema(many=True)


def goods():
    all_food_obj = Data.query.filter(Data.difficult != '未知').order_by(desc(Data.food_type)).limit(50).all()
    all_food_data = single_data_schema.dump(all_food_obj)
    all_food_data = url_parse(all_food_data)
    return jsonify(success_msg(all_food_data))


def goods_type():
    all_food_types_obj = Types.query.filter().all()
    all_types_data = type_schema.dump(all_food_types_obj)
    return jsonify(success_msg(all_types_data))


def goods_search_by_type():
    search_id = request.get_json()
    search_result_obj = Data.query.filter(Data.food_type == search_id['food_type']).order_by(desc(Data.food_type)).limit(50).all()
    search_result = single_data_schema.dump(search_result_obj)
    search_result = url_parse(search_result)
    return jsonify(success_msg(search_result))

def goods_info():
    data = request.get_json()
    food_id = data['id']
    food_data_obj = Data.query.filter_by(id=food_id).all()
    food_data = data_schema.dump(food_data_obj)
    if food_data[0]['pic_path'] != '':
        food_data = step_parse(url_parse(pic_parse(food_data)))
    else:
        food_data = step_parse(url_parse(food_data))
    return jsonify(success_msg(food_data))


def search_goods():
    data = request.get_json()
    if data.get("id"):
        food_id = data.get("id")
        food_obj = Data.query.filter_by(id=food_id).all()
        single_food_data = url_parse(data_schema.dump(food_obj))
        return jsonify(success_msg(single_food_data))
    elif data.get("name"):
        food_name = data.get("name")
        food_obj = Data.query.filter(Data.name.like(f"%{food_name}%")).all()
        single_food_data = url_parse(data_schema.dump(food_obj))
        return jsonify(success_msg(single_food_data))
    else:
        all_food_obj = Data.query.filter().all()
        all_food_data = url_parse(data_schema.dump(all_food_obj))
        return jsonify(success_msg(all_food_data))