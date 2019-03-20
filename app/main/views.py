"""
只处理与主题相关的视图和路由
"""
import os

from . import main
from flask import render_template, session, request, redirect
from .. import db
from ..models import *
import datetime

@main.route('/')
def index_views():
    # 查询Topic中前15条数据并发送到index.html做显示
    topics = Topic.query.limit(15).all()
    #读取Category中的所有内容并发送到index.html显示
    categories = Category.query.all()
    #判断是否有登录的用户
    #判断session中是否有id和loginname
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('index.html',params=locals())

@main.route('/release',methods=['GET','POST'])
def release_views():
    if request.method == 'GET':
        if 'id' in session and 'loginname' in session:
            user = User.query.filter_by(ID=session['id']).first()
            if user.is_author:
                #1.查询category的所有信息
                categories = Category.query.all()
                #2.查询blogtype的所有信息
                blogTypes = BlogType.query.all()
                return render_template('release.html',categories=categories,blogTypes=blogTypes)
        return redirect('/')
    else:
        # 先创建一个Topic实体对象
        topic = Topic()
        # 获取标题(author)为Topic.title赋值
        # 获取文章类型(list)为Topic.blogtype_id赋值
        # 获取内容类型(category)为Topic.category_id赋值
        # 获取内容(content)为Topic.content赋值
        # 从session中获取为Topic.user_id赋值
        # 判断是否有上传图片,处理上传图片,为Topic.images赋值
        # 将Topic对象保存进数据库
        topic.title = request.form['author']
        topic.blogtype_id = request.form['list']
        topic.category_id = request.form['category']
        topic.content = request.form['content']
        topic.user_id = session['id']
        #获取系统时间,为Topic.pub_date赋值
        topic.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if 'picture' in request.files:
            # 获取上传的文件
            f = request.files['picture']
            # 处理文件名
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext = f.filename.split('.')[-1]
            fname = ftime + '.' + ext
            # 将文件名赋值给topic.images
            topic.images = "upload/" + fname

            # 处理上传路径
            basedir = os.path.dirname(os.path.dirname(__file__))
            print(basedir)
            upload_path = os.path.join(basedir,"static/upload",fname)

            # 上传文件
            f.save(upload_path)
        db.session.add(topic)
        return redirect('/')

