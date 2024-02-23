# encoding:utf-8
import os
from datetime import timedelta
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 调试模式是否开启
DEBUG = True
# 是否追踪对象的修改。
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 查询时显示原始SQL语句
SQLALCHEMY_ECHO = False
# session必须要设置key
SECRET_KEY = 'c798ee1f5fd894f6e0ba9fc0d16b8b22'
# mysql数据库连接信息
DATABASE = 'food_flask'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/" + DATABASE

STATIC_PREIFX = "http://127.0.0.1:5000/static/food_img"

# 设置会话过期时间
REMEMBER_COOKIE_DURATION = timedelta(minutes=30)  # 例如设置为14天

# JWT令牌的过期时间
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)

# 上传文件配置
UPLOADED_PHOTOS_DEST = os.path.join(os.path.dirname(__file__), 'static/img')
UPLOADS_AUTOSERVE = True