from flask_marshmallow import Schema
from marshmallow import fields
from app import db
class Types(db.Model):
    __tablename__ = 'food_types'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255), nullable=True,comment='美食种类名称')
    status = db.Column(db.Integer,nullable=False,comment="美食种类状态")
    def __init__(self, type_name):
        self.type_name = type_name
    def __repr__(self):
        return '<Types %r>' % self.type_name
class TypesSchema(Schema):
    id = fields.Integer(attribute='id')
    type_name = fields.String(attribute='type_name')
    status = fields.Integer(attribute='status')