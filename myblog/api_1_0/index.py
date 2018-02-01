#coding=utf8
from . import api

@api.route('/')
def hello_world():
    # redis_store.set('blog1','bbb')
    # session['huaha'] = 'lili'
    return "Hello World! I'm index"