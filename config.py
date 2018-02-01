#coding=utf8
import redis

class Config(object):
    '''工程配置信息'''
    SECRET_KEY = 'shdfsjfh'
    '''数据库配置信息'''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/blog'
    SQLALCHEMY_TRACK_MODIFACTIONS = False

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


class productiveConfig(Config):
    pass

config = {
    'developement':developementConfig,
    'productive':productiveConfig,
}
