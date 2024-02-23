# encoding:utf-8
from flask import jsonify, request
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.model.Data import Data,DataSchema,Data_Single_Schema,Data_list_Schema
from app.model.Types import TypesSchema,Types
from app.utils.message import *
from app.utils.url_parse import url_parse,url_unparse
from sqlalchemy import create_engine
from app.utils.Tools import *
# 数据库连接信息（根据你的数据库信息进行替换）
username = 'root'
password = '123456'
host = '127.0.0.1'
database = 'food_flask'
port = '3306'

# 创建数据库连接
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}', echo=True)
Data_list_Schema = Data_list_Schema(many=True)

def get_all_food():
    food_obj = Data.query.order_by(desc(Data.id)).limit(50).all()
    food_data = Data_list_Schema.dump(food_obj)
    food_data = url_parse(food_data)
    return jsonify(success_msg(food_data))

def update_food():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
        if data['cover'] == 'undefined':
            data['cover'] = './cover.png'
        else:
            cover = url_unparse(data['cover']).replace('http://82.156.147.153:8025/static/food_img/', './')
            data['cover'] = cover
        food_id = data.get("id")
        food_obj = Data.query.filter_by(id=food_id).first()
        update_fields = ['name', 'cover', 'craft','flavour','cost_time','difficult','ingredients','accessories','food_type','step','status']
        try:
            # 使用循环来更新所有提供的字段
            for field in update_fields:
                if field in data:
                    setattr(food_obj, field, data[field])
            db.session.commit()
            return jsonify(success_msg("美食信息更新成功"))
        except SQLAlchemyError as e:
            # 处理数据库错误
            print(f"Error,{str(e)}")
            db.session.rollback()
            return jsonify(error_msg(f"更新失败"))
    else:
        # print(request.form)
        food_id = request.form.get('id')
        food_name = request.form.get('name')
        cost_time = request.form.get('cost_time')
        difficult = request.form.get('difficult')
        craft = request.form.get('craft')
        flavour = request.form.get('flavour')
        ingredients = request.form.get('ingredients')
        accessories = request.form.get('accessories')
        step = request.form.get('step')
        status = request.form.get('status')
        food_type_id = request.form.get('food_type')
        types_obj = Types.query.all()
        # print(f"food_name:{food_name}")
        # print(f"food_type_id:{food_type_id}")
        food_type_name = ''
        for item in types_obj:
            if food_type_id == str(item.id):
                food_type_name = item.type_name
                break
        save_path = f"./app/static/food_img/data/{food_type_name}/{food_name}"
        # 使用 os.makedirs 创建嵌套文件夹
        try:
            os.makedirs(save_path, exist_ok=True)
            print(f"嵌套文件夹 '{save_path}' 创建成功")
        except OSError as error:
            print(f"创建嵌套文件夹时出错: {error}")

        save_cover_path = f'./data/{food_type_name}/{food_name}/cover.jpg'
        if 'cover' in request.files:
            cover = request.files['cover']
            if cover.filename != '':
                cover.save(f'{save_path}/cover.jpg')

        if 'pic_path' in request.files:
            save_pic_path = ''
            pic_path = request.files.getlist('pic_path')
            # 遍历列表，保存每个文件
            for i, file in enumerate(pic_path, start=0):
                filename = f"{i}.jpg"  # 生成文件名，如 0.jpg, 1.jpg
                file.save(f"{save_path}/{filename}")  # 替换为您的目标文件夹路径
                save_pic_path = save_pic_path + filename + ','
                # print(save_pic_path)
            print(pic_path)
            save_pic_path = save_pic_path.rstrip(',')
            # print(save_pic_path)
        data = request.form.to_dict()
        food_obj = Data.query.filter_by(id=food_id).first()
        update_fields = ['name', 'cover', 'craft', 'flavour', 'cost_time', 'difficult', 'ingredients', 'accessories',
                         'food_type', 'step','pic_path' ,'status']
        if 'cover' in request.files:
            data['cover'] = save_cover_path
        else:
            data['cover'] = "./cover.png"
        if 'pic_path' in request.files:
            data['pic_path'] = save_pic_path
        else:
            data['pic_path'] = ''
        print(data)
        try:
            # 使用循环来更新所有提供的字段
            for field in update_fields:
                if field in data:
                    setattr(food_obj, field, data[field])
            db.session.commit()
            return jsonify(success_msg("美食信息更新成功"))
        except SQLAlchemyError as e:
            # 处理数据库错误
            print(f"Error,{str(e)}")
            db.session.rollback()
            return jsonify(error_msg(f"更新失败"))

def add_food():
    if request.headers.get('Content-Type') == 'application/json':
        print("application/json")
        try:
            data = request.get_json()
            print(data)
            if data['cover'] == 'undefined':
                data['cover'] = './cover.png'
            if data['pic_path'] == 'undefined':
                data['pic_path'] = './cover.png'
            food_obj = Data(**data)
            db.session.add(food_obj)
            db.session.commit()
            return success_msg("添加美食成功")
        except KeyError as e:
            print(e)
            return jsonify(error_msg("数据接收错误"))
        except SQLAlchemyError as e:
            print(e)
            # 这里可以添加更详细的数据库异常处理
            return jsonify(error_msg(f"美食已存在"))
    else:
        # print(request.form)
        # print(request.files)
        food_name = request.form.get('name')
        cost_time = request.form.get('cost_time')
        difficult = request.form.get('difficult')
        craft = request.form.get('craft')
        flavour = request.form.get('flavour')
        ingredients = request.form.get('ingredients')
        accessories = request.form.get('accessories')
        step = request.form.get('step')
        status = request.form.get('status')
        food_type_id = request.form.get('food_type')
        types_obj = Types.query.all()
        # print(f"food_name:{food_name}")
        # print(f"food_type_id:{food_type_id}")
        food_type_name = ''
        for item in types_obj:
            if food_type_id == str(item.id):
                food_type_name = item.type_name
                break
        save_path = f"./app/static/food_img/data/{food_type_name}/{food_name}"
        # 使用 os.makedirs 创建嵌套文件夹
        try:
            os.makedirs(save_path, exist_ok=True)
            print(f"嵌套文件夹 '{save_path}' 创建成功")
        except OSError as error:
            print(f"创建嵌套文件夹时出错: {error}")

        save_cover_path = f'./data/{food_type_name}/{food_name}/cover.jpg'
        if 'cover' in request.files:
            cover = request.files['cover']
            if cover.filename != '':
                print(f"{save_path}/cover.jpg")
                cover.save(f'{save_path}/cover.jpg')
        save_pic_path = ''
        if 'pic_path' in request.files:
            pic_path = request.files.getlist('pic_path')
            print(pic_path)
            # 遍历列表，保存每个文件
            for i, file in enumerate(pic_path, start=0):
                filename = f"{i}.jpg"  # 生成文件名，如 0.jpg, 1.jpg
                file.save(f"{save_path}/{filename}")  # 替换为您的目标文件夹路径
                save_pic_path = save_pic_path + filename + ','
                # print(save_pic_path)
            save_pic_path = save_pic_path.rstrip(',')
            # print(save_pic_path)
        food_obj = Data(name=food_name, cost_time=cost_time, difficult=difficult, flavour=flavour,
                        food_type=food_type_id, ingredients=ingredients, accessories=accessories, step=step,
                        status=status, pic_path=save_pic_path, cover=save_cover_path, craft=craft)
        db.session.add(food_obj)
        db.session.commit()
        return jsonify(success_msg("接收成功"))

def data_init():
    try:
        all_data_import()
        return jsonify(success_msg("初始化成功"))
    except Exception as e:
        print(e)
        return jsonify(error_msg("初始化失败"))

def single_data_import(csv_path,table_name):
    """
    将单个CSV导入数据库中
    :param csv_path:CSV文件路径
    :param table_name:导入的表名
    :return:
    """
    csv = pd.read_csv(csv_path)
    # 为数据添加 'status' 列，其值为 1
    csv['status'] = 1
    # 将数据导入到 MySQL 数据库中（假设表名为 your_table）
    csv.to_sql(table_name, con=engine, if_exists='append', index=False)

def all_data_import():
    """
    将目录下所有CSV文件导入到MYSQL中
    :return:
    """
    food_data_path_prefix = "./app/static/food_img/data/"
    food_data_table = 'food_data'
    food_types_table = 'food_types'
    csv_files = find_csv_files(food_data_path_prefix)
    for file in csv_files:
        single_data_import(file.replace('\\', '/'),food_data_table)
    single_data_import('all_types.csv',food_types_table)

