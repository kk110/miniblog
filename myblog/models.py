#coding=utf8
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    '''用户'''

    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128),nullable=False)
    is_admin = db.Column(db.Boolean(),nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verif_password(self,password):
        return check_password_hash(self.password_hash,password)