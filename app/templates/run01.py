from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#从flask_script包中导入Manager类,用于管理项目
from flask_script import Manager

#从flask_migrate包中导入Migrate,MigrateCommand,用于做数据库的迁移
from flask_migrate import Migrate,MigrateCommand

#导入pymysql并将其视为 mysqldb
# import pymysql
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 通过app指定连接数据库信息
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flask"
#取消SQLAlchemy的信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#为app指定启动模式
app.config['debug']=True
# 创建数据库应用实例 - db
db = SQLAlchemy(app)

#创建Manager对象并指定要管理的应用(app)
manager = Manager(app)
#创建Migrate对象,指定关联的app和db
migrate = Migrate(app,db)
#为manager增加子命令,允许做数据库迁移的子命令
#为manager增加一个叫 db(自己取名) 的子命令,该子命令的具体操作由MigrateCommend来提供
manager.add_command("db",MigrateCommand)

#创建实体类Users,映射到数据库中叫users表
#创建字段 -id,主键,自增
#创建字段 -username,长度为80的字符串,不允许为空,值唯一
#age ,整数,允许为空
#创建字段-email,长度为120,值唯一,不为空
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    uname = db.Column(db.String(80),nullable=False,unique=True,index=True)
    age = db.Column(db.Integer,nullable=True)
    email = db.Column(db.String(120),unique=True,nullable=False)
    #增加一个列,isActive
    isActive = db.Column(db.Boolean,default=True)

#实体类 Student,Teacher,Course
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer,nullable=False)
    isActive = db.Column(db.Boolean, default=True)

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer,nullable=False)
    #增加一个属性 - isActive,默认值为True
    isActive = db.Column(db.Boolean,default=True)

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer,primary_key=True)
    cname=db.Column(db.String(30),nullable=False)


@app.route('/')
def index():
    return "asdfffffffffh"

# #删除所有数据表
# db.drop_all()
#
# #将创建好的实体类映射回数据库,生成表
# #前提是数据表不存在
# db.create_all()



if __name__ == "__main__":
    #app.run(debug=True)
    #通过manager启动服务
    manager.run()
    #通过manager启动服务
    # python3 run01.py sunserver
    # 问题1:无法指定调试模式(debug=True)
    # 解决方案:app.config['DEBUG']=True
    # 问题2:无法指定启动主机地址(host=0.0.0.0)
    # 解决方案:python3 run01.py runserver --host 0.0.0.0
    # 问题3:无法指定启动端口(port=5555)
    # 解决方案:python3 run01.py runserver --port 5555
    # 解决问题2和问题3
    # python3 run01.py sunserver --host 0.0.0.0 --port 5555
