# encoding:utf-8
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.model.User import User, UserSchema, UserUpdateSchema
from app.utils.message import *

user_schema = UserSchema(many=True)
user_udpate_schema = UserUpdateSchema(many=True)


def get_all_user():
    all_user_obj = User.query.filter().all()
    all_user_data = user_schema.dump(all_user_obj)
    return jsonify(success_msg(all_user_data))

def search_user():
    data = request.get_json()
    if data.get("id"):
        user_id = data.get("id")
        user_obj = User.query.filter_by(id=user_id).all()
        single_user_data = user_schema.dump(user_obj)
        return jsonify(success_msg(single_user_data))
    elif data.get("name"):
        username = data.get("name")
        user_obj = User.query.filter_by(name=username).all()
        single_user_data = user_schema.dump(user_obj)
        return jsonify(success_msg(single_user_data))
    else:
        all_user_obj = User.query.filter().all()
        all_user_data = user_schema.dump(all_user_obj)
        return jsonify(success_msg(all_user_data))

def update_user():
    data = request.get_json()
    user_id = data.get("id")
    if not user_id:
        return jsonify(error_msg("json需要有id"))
    user_obj = User.query.filter_by(id=user_id).first()
    if not user_obj:
        return jsonify(error_msg("用户不存在"))
    update_fields = ['name', 'phone', 'is_admin', 'pic', 'status', 'password']
    data_changed = False
    try:
        for field in update_fields:
            if field in data:
                # 对密码字段进行特殊处理
                if field == 'password':
                    # 检查密码是否已更改
                    if not user_obj.check_password(data['password']):
                        user_obj.set_password(data['password'])
                        data_changed = True
                else:
                    # 检查其他字段是否已更改
                    if getattr(user_obj, field) != data[field]:
                        setattr(user_obj, field, data[field])
                        data_changed = True
        if not data_changed:
            return jsonify(error_msg("请勿重复更新"))
        db.session.commit()
        return jsonify(success_msg("用户信息更新成功"))
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(error_msg(f"更新失败, {str(e)}"))

def add_user():
    data = request.get_json()
    print(data)
    # 获取用户提交的数据
    name = data['name']
    email = data['email']
    phone = data['phone']
    password = data['password']
    is_admin = data['is_admin']
    # 检查用户是否已存在
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(error_msg("该邮箱已被注册"))
    # 创建新用户
    new_user = User(name=name, email=email, phone=phone, password=password,is_admin=is_admin)
    db.session.add(new_user)
    db.session.commit()
    resp = {
        'msg': '添加成功',
        'code': 200
    }
    return jsonify(resp)