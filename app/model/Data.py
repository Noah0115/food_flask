from flask_marshmallow import Schema
from marshmallow import fields
from app import db
from app import ma


class Data(db.Model):
    __tablename__ = 'food_data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True, comment='美食名称')
    cover = db.Column(db.String(255), nullable=True, comment='美食封面路径')
    craft = db.Column(db.String(255), nullable=True, comment='工艺')
    flavour = db.Column(db.String(255), nullable=True, comment='口味')
    cost_time = db.Column(db.String(255), nullable=True, comment='烹饪时间')
    difficult = db.Column(db.String(255), nullable=True, comment='烹饪难度')
    ingredients = db.Column(db.String(255), nullable=True, comment='主料')
    accessories = db.Column(db.String(255), nullable=True, comment='辅料')
    step = db.Column(db.Text(), nullable=False, comment='做法步骤')
    pic_path = db.Column(db.String(255), nullable=False, comment='步骤图路径')
    food_type = db.Column(db.String(255), nullable=False, comment='美食种类')
    status = db.Column(db.Integer, nullable=False, comment="美食状态")

    def __init__(self, name, cover, craft, flavour, cost_time, difficult, ingredients, accessories, step, food_type,
                 pic_path='none', status=1):
        self.name = name
        self.cover = cover
        self.craft = craft
        self.flavour = flavour
        self.cost_time = cost_time
        self.difficult = difficult
        self.ingredients = ingredients
        self.accessories = accessories
        self.step = step
        self.pic_path = pic_path
        self.food_type = food_type
        self.status = status

    def __repr__(self):
        return '<Data %r>' % self.name


class DataSchema(Schema):
    id = fields.Integer(attribute='id')
    name = fields.String(attribute='name')
    cover = fields.String(attribute='cover')
    craft = fields.String(attribute='craft')
    flavour = fields.String(attribute='flavour')
    cost_time = fields.String(attribute='cost_time')
    difficult = fields.String(attribute='difficult')
    ingredients = fields.String(attribute='ingredients')
    accessories = fields.String(attribute='accessories')
    pic_path = fields.String(attribute='pic_path')
    food_type = fields.String(attribute='food_type')
    step = fields.String(attribute='step')
    status = fields.Integer(attribute='status')


class Data_list_Schema(Schema):
    id = fields.Integer(attribute='id')
    name = fields.String(attribute='name')
    cover = fields.String(attribute='cover')
    craft = fields.String(attribute='craft')
    flavour = fields.String(attribute='flavour')
    cost_time = fields.String(attribute='cost_time')
    difficult = fields.String(attribute='difficult')
    ingredients = fields.String(attribute='ingredients')
    accessories = fields.String(attribute='accessories')
    food_type = fields.String(attribute='food_type')
    step = fields.String(attribute='step')
    status = fields.Integer(attribute='status')


class Data_Single_Schema(Schema):
    id = fields.Integer(attribute='id')
    name = fields.String(attribute='name')
    cover = fields.String(attribute='cover')
    flavour = fields.String(attribute='flavour')
    difficult = fields.String(attribute='difficult')
    food_type = fields.String(attribute='food_type')
    status = fields.Integer(attribute='status')
