# encoding:utf-8
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.model.News import News, NewsSchema
from app.utils.message import *

news_schema = NewsSchema(many=True)

# 查询全部公告
def get_all_news():
    news_obj = News.query.filter_by(status=1).all()
    news_data = news_schema.dump(news_obj)
    print(news_data)
    return success_msg(news_data)

# 查询全部公告
def get_all_news_admin():
    news_obj = News.query.filter_by().all()
    news_data = news_schema.dump(news_obj)
    print(news_data)
    return success_msg(news_data)

def add_news():
    try:
        data = request.get_json()
        title = data['title']
        content = data['content']
        news_obj = News(title=title, content=content)
        db.session.add(news_obj)
        db.session.commit()
        return success_msg("添加公告成功")
    except KeyError:
        return jsonify(error_msg("数据接收错误"))
    except SQLAlchemyError as e:
        # 这里可以添加更详细的数据库异常处理
        return jsonify(error_msg(f"公告已存在"))


def update_news():
    data = request.get_json()
    news_id = data.get("id")
    news_obj = News.query.filter_by(id=news_id).first()
    update_fields = ['title', 'content', 'status']
    try:
        # 使用循环来更新所有提供的字段
        for field in update_fields:
            if field in data:
                setattr(news_obj, field, data[field])
        db.session.commit()
        return jsonify(success_msg("公告信息更新成功"))
    except SQLAlchemyError as e:
        # 处理数据库错误
        print(f"Error,{str(e)}")
        db.session.rollback()
        return jsonify(error_msg(f"更新失败,不能与其他公告标题一致"))
