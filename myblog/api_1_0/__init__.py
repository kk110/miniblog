from flask import Blueprint

api = Blueprint('api_1_0',__name__,
                static_folder='/myblog/static')

from . import index