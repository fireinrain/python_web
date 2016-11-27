#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

from app import db

class Flask_tdd(db.Model):

    __tablename__ = 'flask_tdd'

    post_id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)

    def __init__(self,title,text):
        self.title = title
        self.text = text

    def __str__(self):
        return '<title{}>'.format(self.body)