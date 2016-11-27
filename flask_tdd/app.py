#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

import sqlite3
import os


from flask import (Flask, request,session,g,redirect,
                    url_for,abort,render_template,flash,jsonify
                   )

from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
# flask app相关配置
DATABASE = 'flaskr.db'
DATABASE_PATH=os.path.join(basedir,DATABASE)
DEBUG = True
SECRET_KEY = 'i love mayuyu'
USERNAME = 'admin'
PASSWORD = 'admin'

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS=True

app=Flask(__name__)
#导入配置
app.config.from_object(__name__)
db = SQLAlchemy(app)

import models

# # 链接数据库
# def connect_db():
#     """connect to the database"""
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv
#
# # 创建数据库
# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('database.sql',mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()
#
# # 打开数据库链接
# def get_db():
#     if not hasattr(g,'sqlite_db'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db
#
# # 关闭数据库链接
# @app.teardown_appcontext
# def close_db(error):
#     if hasattr(g,'sqlite_db'):
#         g.sqlite_db.close()




# 视图开始
@app.route('/')
def index():
    # db = get_db()
    # cur = db.execute('select * from entries order by id desc')
    # entries=cur.fetchall()

    # sqlalchemy实现
    entries = db.session.query(models.Flask_tdd)
    return render_template('index.html',entries=entries)

# 登录视图
@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html',error=error)


# 登出视图
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('index'))


# 添加视图
@app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(404)
    # db = get_db()
    # db.execute(
    #     'insert into entries (title,text) values (?,?)',
    #     [request.form['title'],request.form['text']]
    # )
    # db.commit()

    # sqlachemy实现
    new_entry = models.Flask_tdd(request.form['title'],request.form['text'])
    db.session.add(new_entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('index'))

# 删除api
@app.route('/delete/<post_id>',methods=['GET'])
def delete_entry(post_id):
    result = {'status':0,'message':'Error'}
    try:
        # db = get_db()
        # db.execute('delete from entries where id ='+post_id)
        # db.commit()

        # sqlachemy实现
        new_id = post_id
        db.session.query(models.Flask_tdd).filter_by(post_id=new_id).delete()
        db.session.commit()
        result = {'status':1,'message':'Post Delete'}
    except Exception as e:
        result = {'status':0,'message':repr(e)}

    return jsonify(result)

# @app.route('/')
# def hello():
#     return "Hello,World"

if __name__=='__main__':
    # init_db()
    app.run(host='0.0.0.0',port=80,debug=True)





























































































