#coding=utf-8
from flask import Flask,session
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from myblog import create_app,db
from flask import render_template
from datetime import datetime


app = create_app('developement')
# @app.route('/index')
# def s_index():
#     return 'outter index'
#
# @app.errorhandler(404)
# def page_not(e):
#     return render_template('404.html'),404

@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

# 数据库迁移和扩展
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    app.run()
