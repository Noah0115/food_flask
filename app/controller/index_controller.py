# -*- coding: utf-8 -*-
import app
from sqlalchemy import and_, func
from app.utils.url_parse import *
from flask import jsonify, request
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from urllib.parse import quote
from app.config import STATIC_PREIFX
from app.model.User import User
from app.model.Data import Data, DataSchema, Data_Single_Schema
from app.model.Types import Types, TypesSchema
from app import db, login_manager
from app.utils.message import *

data_schema = DataSchema(many=True)
single_data_schema = Data_Single_Schema(many=True)
types_schema = TypesSchema(many=True)


@login_required
def index():
    if current_user.is_authenticated():
        print("true")
        user_id = current_user.id  # 假设您有一个 current_user 对象
        user_info = User.query.filter_by(id=user_id).first()
        resp = {
            "name": user_info.name,
            "pic": user_info.pic
        }
        return jsonify(success_msg(resp))
    else:
        print("false")
        return jsonify(success_msg("目前是游客状态"))


def get_food_index():
    jiachang_obj = Data.query.filter(and_(Data.difficult != '未知', Data.food_type == 1)).limit(7)
    haixian_obj = Data.query.filter(and_(Data.difficult != '未知', Data.food_type == 4)).limit(7)
    dianxin_obj = Data.query.filter(and_(Data.difficult != '未知', Data.food_type == 11)).limit(7)

    jiachang_data = single_data_schema.dump(jiachang_obj)
    haixian_data = single_data_schema.dump(haixian_obj)
    dianxin_data = single_data_schema.dump(dianxin_obj)
    jiachang_data = url_parse(jiachang_data)
    haixian_data = url_parse(haixian_data)
    dianxin_data = url_parse(dianxin_data)
    all_data_tuple = (jiachang_data, haixian_data, dianxin_data)
    return jsonify(success_msg(all_data_tuple))


def food_search():
    data = request.get_json()
    search_name = data["search_name"]
    results_obj = Data.query.filter(Data.name.ilike(f'%{search_name}%')).limit(3).all()
    results = single_data_schema.dump(results_obj)
    results = url_parse(results)
    return jsonify(results)


def data_anl_bar():
    try:
        # 只进行一次查询：对 difficult 字段的每个值进行分组并计算每组的数量
        counts = db.session.query(Data.difficult, func.count(Data.difficult)).group_by(Data.difficult).all()

        # 提取 distinct values 和 counts
        distinct_values_list = [value for value, _ in counts]
        count_list = [count for _, count in counts]

        # 返回 JSON 结果
        return jsonify(success_msg([distinct_values_list, count_list]))

    except Exception as e:
        # 处理可能发生的异常
        return jsonify(error_msg(str(e)))


def data_anl_pie():
    try:
        # 查询 food_type 字段不同值的数量
        food_type_count = db.session.query(Data.food_type, func.count(Data.food_type)).group_by(Data.food_type).all()

        # 查询 Types 表中的所有记录
        types_obj = Types.query.all()

        # 将 Types 对象转换为 id 到 type_name 的映射
        types_map = {str(type_item.id): type_item.type_name for type_item in types_obj}

        # 根据 food_type_count 和 types_map 创建最终结果
        final_result = [{"value": count, "name": types_map.get(food_type, "未知类型")} for food_type, count in
                        food_type_count]

        # 返回 JSON 结果
        return jsonify(success_msg(final_result))

    except Exception as e:
        # 记录异常信息并返回错误消息
        # 考虑记录日志或打印更详细的异常信息
        print(f"Error in data_anl_pie: {e}")
        return jsonify(error_msg(str(e)))


def data_anl_pie_flavour():
    try:
        # 查询 food_type 字段不同值的数量
        flavour_count = db.session.query(Data.flavour, func.count(Data.flavour)).group_by(Data.flavour).all()
        formatted_data = [{'value': value, 'name': name} for name, value in flavour_count]
        # 打印处理后的数据
        # 计算value值的总和
        total_value = sum(entry['value'] for entry in formatted_data)
        print(formatted_data)
        print(total_value)
        # 返回 JSON 结果
        return jsonify(success_msg([formatted_data, [total_value]]))

    except Exception as e:
        # 记录异常信息并返回错误消息
        # 考虑记录日志或打印更详细的异常信息
        print(f"Error in data_anl_pie: {e}")
        return jsonify(error_msg(str(e)))


def data_rader():
    # result = db.session.query(Data.name, Data.flavour, Data.cost_time, Data.difficult).all()  # 全部数据
    result = db.session.query(Data.name, Data.flavour, Data.cost_time, Data.difficult).filter(Data.food_type == '1').all()

    # 将查询结果转换为字典列表
    foods_list = []
    food_name_ls = []
    flavour_dict = {'五香味': 1, '咖喱味': 2, '咸鲜味': 3, '奶香味': 4, '家常味': 5, '果味': 6, '椒麻味': 7, '甜味': 8,
                    '糖醋味': 9, '芥末味': 10, '茄汁味': 11, '葱香味': 12, '蒜香味': 13, '豆瓣味': 14, '酱香味': 15,
                    '酸味': 16, '酸甜味': 17, '酸辣味': 18, '香辣味': 19, '麻辣味': 20, '黑椒味': 21, '其它口味': 22}
    difficult_dict = {'未知': 1, '新手尝试': 2, '初级入门': 3, '初中水平': 4, '中级掌勺': 5, '高级厨师': 6}
    for food in result:
        food_name_ls.append(food.name)
        if food.cost_time in ["数天", "数小时", "未知"]:
            processed_cost_time = 60
        else:
            # 尝试提取数字部分
            digits = ''.join(filter(str.isdigit, food.cost_time))
            processed_cost_time = int(digits) if digits else 0
        foods_list.append({
            "value":[flavour_dict.get(food.flavour, 0), processed_cost_time,difficult_dict.get(food.difficult, 0)],
            "name":food.name
        })
    # print(food_name_ls)
    # print(foods_list)
    data = {
        "data_name":food_name_ls,
        "data":foods_list
    }
    return jsonify(success_msg(data))
