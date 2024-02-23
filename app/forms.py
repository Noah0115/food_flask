# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class RegisterForm(FlaskForm):
    name = StringField('name', [validators.DataRequired("用户名不能为空")])
    email = StringField('email', [validators.DataRequired("邮箱不能为空"), validators.Email("无效的邮箱地址")])
    phone = StringField('phone')
    password = PasswordField('password', [
        validators.DataRequired("密码不能为空"),
        validators.Length(min=8, message="密码长度至少 8 个字符")
    ])

class LoginForm(FlaskForm):
    email = StringField('邮箱', [validators.DataRequired("邮箱不能为空"), validators.Email("无效的邮箱地址")])
    password = PasswordField('密码', [validators.DataRequired("密码不能为空")])
    remember = StringField('记住我')
