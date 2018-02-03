#coding=utf8
from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class Role(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    permissions = db.Column(db.Integer)
    user = db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>'%self.name

class User(db.Model):
    '''用户'''

    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False,index=True)
    email = db.Column(db.String(64),unique=True,nullable=False,index=True)
    password_hash = db.Column(db.String(128),nullable=False)
    confirmed = db.Column(db.Boolean,default=False)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))



    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verif_password(self,password):
        return check_password_hash(self.password_hash,password)