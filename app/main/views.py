"""
只处理与主题相关的视图和路由
"""
from . import main
from flask import render_template, session
from .. import db
from ..models import *

@main.route('/')
def index_views():
    #读取Category中的所有内容并发送到index.html显示
    categories = Category.query.all()
    #判断是否有登录的用户
    #判断session中是否有id和loginname
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('index.html',params=locals())