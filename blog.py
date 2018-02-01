#coding=utf-8
from flask import Flask,session
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from myblog import create_app,db

app = create_app('developement')

# 数据库迁移和扩展
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    app.run()
