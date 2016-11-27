#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

from app import  db
from models import  Flask_tdd

# create database and tables
db.create_all()

# commit
db.session.commit()