'''
与用户相关的路由和视图
'''

from . import users
from flask import render_template, redirect
from .. import db
from ..models import *
from flask import request
from flask import session,make_response


@users.route('/login',methods=["GET","POST"])
def login_views():
    if request.method == "GET":
        #获取请求原地址,将地址保存进cookies
        resp = make_response(render_template('login.html'))
        url = request.headers.get("Referer",'/')
        resp.set_cookie('url',url)
        return resp
    else:
        # 1.接收提交过来的用户名和密码
        uname = request.form['username']
        upwd = request.form['password']
        # 2.验证用户名和密码的有效性
        user = User.query.filter(User.loginname==uname,User.upwd==upwd).first()
        # 3.给出响应
        if user:
            # 登陆成功
            # 1.将登录信息保存进session
            session['id'] = user.ID
            session['loginname'] = user.loginname
            # 2.从哪来回哪去(从cookies中获取请求原地址)
            url = request.cookies.get('url')
            return redirect(url)
        else:
            #登录失败
            return render_template('login.html')


@users.route('/register')
def register_views():
    return render_template('register.html')

@users.route('/logout')
def logout_views():
    #获取请求源地址
    url = request.headers.get('Referer','/')
    #判断session中是否有登录信息,如果有则删除
    if 'id' in session and 'loginname' in session:
        del session['id']
        del session['loginname']
    #重定向到源地址
    return redirect(url)


@users.route('/list')
def list_views():
    pass

























