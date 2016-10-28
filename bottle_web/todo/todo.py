#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

import sqlite3
from bottle import route,run,template,request,static_file,error

@route('/todo')
def todo_list():
    conn=sqlite3.connect('todo.db')
    cursor=conn.cursor()
    cursor.execute('SELECT id,task From todo WHERE status LIKE "1"')
    result=cursor.fetchall()
    cursor.close()

    output = template('make_table.html',rows=result)
    return output
    # return str(result)

@route('/new',method='GET')
def new_item():
    if request.GET.get('save','').strip():      #如果提交了

        new=request.GET.get('task','').strip()

        conn=sqlite3.connect('todo.db')
        c=conn.cursor()

        c.execute('INSERT INTO todo (task,status) VALUES (?,?)',(new,1))
        new_id=c.lastrowid

        conn.commit()
        c.close()
        return "<p> the new task was inserted into the database,the id is %s</p>" % new_id
    else:
        return template('new_task.html')

@route('/edit/<num:int>',method='GET')
def edit_item(num):
    if request.GET.get('save'):
        edit=request.GET.get('task').strip()
        status=request.GET.get('status').strip()

        if status=='open':
            status=1
        else:
            status=0

        conn=sqlite3.connect('todo.db')
        c=conn.cursor()
        c.execute('UPDATE todo SET task=?,status=? WHERE id LIKE ?',(edit,status,num))
        conn.commit()

        return "<p>the item number %s was successfully update" % num
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute('SELECT task FROM todo WHERE id LIKE ?',(str(num)))
        cur_data=c.fetchone()

        return template('edit_task.html',old=cur_data,num=num)

@route('/item/<item:re:[0-9]+>')
def show_item(item):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT task FROM todo WHERE id LIKE ?', (item))
    result=c.fetchall()
    if not result:
        return "the item number does not exit"
    else:
        return 'task:%s' % result[0]

@route('/help')
def help():
    static_file('help.html',root='.')

@route('/json/<json:re:[0-9]+>')
def show_json():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT task FROM todo WHERE id LIKE ?', (json))
    result = c.fetchall()

    if not result:
        return {'task':'this item does not exist'}
    else:
        return {'task':result[0]}

@error(404)
def mistake404(code):
    return 'sorry the page does not exist'

@error(403)
def mistake403(code):
    return 'there is a mistake in your url'



run(host='localhost',port=8000,debug=True,reloader=True)
