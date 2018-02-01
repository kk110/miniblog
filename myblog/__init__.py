#coding=utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis
from config import Config,config
import logging
from logging.handlers import RotatingFileHandler
from flask_mail import Mail

# 项目初始化
db = SQLAlchemy()
redis_store = None
csrf = CSRFProtect()
mail = Mail()

# logging
logging.basicConfig(level=logging.DEBUG)
file_log_handler = RotatingFileHandler('logs/log',maxBytes=1024*1024*100, backupCount=10)
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)

# 创建app的工厂函数
def create_app(app_name):
    app = Flask(__name__)
    app.config.from_object(config[app_name])
    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
    csrf.init_app(app)
    Session(app)
    mail.init_app(app)

    import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix='/api/v1.0')

    return app


