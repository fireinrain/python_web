#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

import sqlite3

con = sqlite3.connect('todo.db')         #在当前目录下创建db文件
con.execute('create table todo(id INTEGER PRIMARY KEY,task CHAR(100) NOT NULL,status bool NOT NULL) ')      #创建todo list表，包含id，任务，和执行状态
con.execute("INSERT INTO todo(task,status) VALUES ('read-a-bite-of-python',1)")
con.execute("INSERT INTO todo(task,status) VALUES ('visit the python web site',0)")
con.execute("INSERT INTO todo(task,status) VALUES ('learning the oop of python',1)")
con.execute("INSERT INTO todo(task,status) VALUES ('think about the python framework',1)")
con.commit()
