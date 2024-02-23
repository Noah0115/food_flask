from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_marshmallow import Schema
from marshmallow import fields
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'food_userinfo'
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(255), nullable=False,comment="用户名")
    email = db.Column(db.String(255), nullable=False, unique=True,comment="邮箱")
    phone = db.Column(db.String(255), nullable=False,comment="手机号")
    password_hash = db.Column(db.String(255), nullable=False,comment="密码")  # 添加密码哈希字段
    is_admin = db.Column(db.Boolean, default=False, nullable=False,comment="是否为管理员")  # 新增 is_admin 字段
    pic = db.Column(db.String(255), nullable=False,comment="头像路径")
    status = db.Column(db.Integer,nullable=False,comment="账号状态")
    def __init__(self,name, email, phone, password, is_admin=False,pic='static/img/default.png',status=1):
        self.name = name
        self.email = email
        self.phone = phone
        self.set_password(password)  # 在初始化时设置密码哈希值
        self.is_admin = is_admin  # 设置用户是否是管理员
        self.pic = pic
        self.status = status


    def __repr__(self):
        return '<User %r>' % self.name

    # 添加密码哈希相关的方法
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 实现 is_active 方法
    def is_active(self):
        return True  # 返回 True 表示用户是活动的，可以登录

class UserSchema(Schema):
    id = fields.Integer(attribute='id')
    name = fields.String(attribute='name')
    email = fields.String(attribute='email')
    phone = fields.String(attribute='phone')
    is_admin = fields.Boolean(attribute='is_admin')
    pic = fields.String(attribute='pic')
    status = fields.Integer(attribute='status')

class UserUpdateSchema(Schema):
    id = fields.Integer(attribute='id')
    name = fields.String(attribute='name')
    email = fields.String(attribute='email')
    password_hash = fields.String(attribute='password_hash')
    phone = fields.String(attribute='phone')
    is_admin = fields.Boolean(attribute='is_admin')
    pic = fields.String(attribute='pic')
    status = fields.Integer(attribute='status')