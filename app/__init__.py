'''
app包包含所有的程序处理的相关文件(静态文件,模板文件,实体类以及各个业务处理
__init__.py:
    1.构建Flask程序实例以及配置
    2.构建SQLAlchemy数据库实例
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#声明SQLAlchemy的实例
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #指定配置
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'tfgyuhjiok'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/blog"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #关联db和app
    db.init_app(app)
    #将main蓝图程序与app相关联
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #将users蓝图程序与app相关联
    from .users import users as users_bluepring
    app.register_blueprint(users_bluepring)

    #返回Flask实例
    return app

