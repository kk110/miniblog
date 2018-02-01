#coding=utf8
import redis

class Config(object):
    '''工程配置信息'''
    SECRET_KEY = 'shdfsjfh'
    '''数据库配置信息'''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 将session保存到redis
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400


class developementConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'klk_1115@163.com'
    MAIL_PASSWORD = 'studyuse1115'
    MAIL_DEFAULT_SENDER = 'cooladmin<klk_1115@163.com>'


class productiveConfig(Config):
    pass

config = {
    'developement':developementConfig,
    'productive':productiveConfig,
}
