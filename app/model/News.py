from flask_marshmallow import Schema
from marshmallow import fields
from app import db
from app import ma


class News(db.Model):
    __tablename__ = 'food_news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True, unique=True,comment='公告标题')
    content = db.Column(db.Text, nullable=True, comment='公告内容')
    status = db.Column(db.Integer, nullable=False, comment="公告状态")

    def __init__(self, title, content, status=1):
        self.title = title
        self.content = content
        self.status = status

    def __repr__(self):
        return '<News %r>' % self.title


class NewsSchema(Schema):
    id = fields.Integer(attribute='id')
    title = fields.String(attribute='title')
    content = fields.String(attribute='content')
    status = fields.Integer(attribute='status')
