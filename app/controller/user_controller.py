# encoding:utf-8
from flask import jsonify, request
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from app.forms import RegisterForm, LoginForm
from app.model.User import User,UserSchema
from app import db, login_manager
from app.utils.message import *
from flask_wtf.csrf import generate_csrf

user_schema = UserSchema(many=True)
def register():
    """
    注册新用户。
    该函数处理新用户的注册过程。它验证用户提交的表单数据，
    检查用户是否已存在，在数据库中创建新用户，并将用户重定向到登录页面
    注册成功后。
    Returns:
        如果表单数据有效并且用户注册成功，返回200
    """
    print("Register")
    data = request.get_json()
    print(data)
    # 获取用户提交的数据
    name = data['name']
    email = data['email']
    phone = data['phone']
    password = data['password']
    # 检查用户是否已存在
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(error_msg("该邮箱已被注册"))
    # 创建新用户
    new_user = User(name=name, email=email, phone=phone, password=password)
    db.session.add(new_user)
    db.session.commit()
    resp = {
        'msg': '注册成功，请登录!',
        'code': 200
    }
    return jsonify(resp)


def login():
    """
    用户登录函数

    如果用户已登录，则重定向到受保护的页面。
    如果用户提交了有效的登录表单，则验证用户凭据并将用户标记为已登录。
    如果用户验证失败，则显示错误消息。
    :return: 响应信息
    """
    # if current_user.is_authenticated:
    #     # 如果用户已登录，重定向到受保护的页面
    #     return jsonify(success_msg("已登录，正在跳转主页"))
    if request.method == "POST":
        data = request.get_json()
        email = data['email']  # 修改为使用邮箱作为登录凭据
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            # 用户验证成功，将用户标记为已登录
            # 可以使用 Flask-Login 或自己的会话管理逻辑来处理登录状态
            login_user(user, remember=True)
            print("登录成功")
            return jsonify(success_msg("登录成功"))
        else:
            return jsonify(error_msg("登录失败，密码错误"))
    else:
        return jsonify(success_msg("尚未登录,目前为游客模式"))


def profile():
    print("查看个人信息")
    data = request.get_json()
    email = data['email']  # 修改为使用邮箱作为登录凭据
    print(email)
    user = User.query.filter_by(email=email).all()
    profile = user_schema.dump(user)
    if user:
        return jsonify(success_msg(profile))
    else:
        return jsonify(error_msg("用户不存在"))

@login_required
def logout():
    if logout_user():  # 使用 Flask-Login 注销用户
        return jsonify(success_msg("您已成功登出"))
    return jsonify(error_msg("登出失败"))


@login_manager.user_loader
def load_user(user_id):
    # 使用用户 ID 查询用户对象
    return User.query.get(int(user_id))


def get_csrf():
    # 调用函数生成csrf token
    csrf_token = generate_csrf()
    print(csrf_token)
    # 设置cookie传给前端
    return csrf_token


def check_current_login():  # 检查当前登录用户
    if current_user.is_authenticated:
        # 当前有用户登录
        return f"当前登录的用户是: {current_user.username}"
    else:
        # 当前没有用户登录
        return "当前没有用户登录"
