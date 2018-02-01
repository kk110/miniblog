#coding=utf8
from . import api
from flask_mail import Message
from myblog import mail


@api.route('/')
def hello_world():
    # redis_store.set('blog1','bbb')
    # session['huaha'] = 'lili'
    # msg = Message(subject='博客测试',recipients='klk_1115@163.com',body='邮件内容')
    # mail.send(msg)
    return "Hello World! I'm index"