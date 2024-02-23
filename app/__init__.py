import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_uploads import configure_uploads
from flask_cors import *

from flask_socketio import SocketIO

# 创建Flask应用实例
db = SQLAlchemy()  # 数据库实例
login_manager = LoginManager()  # 登录管理实例
migrate = Migrate()  # 数据库迁移实例
ma = Marshmallow()
socketio = SocketIO(ping_timeout=9999,cors_allowed_origins="*")
def create_app() -> Flask:
    """创建Flask应用实例并进行初始化设置。

    Returns:
        Flask: 初始化设置后的Flask应用实例。
    """
    app = Flask(__name__)
    CORS(app, resource=r'/*')
    # CORS(app, supports_credentials=True)
    app.config.from_object('app.config')
    # app.config.from_envvar('FLASKR_CONFIGS')

    initialize_extensions(app)
    register_blueprints(app)
    configure_api_resources(app)
    socketio.init_app(app, cors_allowed_origins="*")
    return app


def initialize_extensions(app: Flask) -> None:
    """初始化扩展，包括数据库、登录管理、数据库迁移、邮件和文件上传。

    Args:
        app (Flask): Flask应用实例。
    """
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    from app.controller.api_controller import photos
    configure_uploads(app, photos)


def register_blueprints(app: Flask) -> None:
    """注册蓝图，包括主页、用户、事件和提醒蓝图。

    Args:
        app (Flask): Flask应用实例。
    """
    from app.views.index_view import index_blueprint
    from app.views.user_view import user_blueprint
    from app.views.goods_view import goods_blueprint
    from app.views.back_view import back_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(goods_blueprint, url_preifx='/')
    app.register_blueprint(back_blueprint, url_preifx='/back')


def configure_api_resources(app: Flask) -> None:
    """配置API资源，包括文件上传资源。

    Args:
        app (Flask): Flask应用实例。
    """
    api = Api(app)

    from app.controller.api_controller import (
        FileUploadResource
    )
    api.add_resource(FileUploadResource, '/api/upload')
