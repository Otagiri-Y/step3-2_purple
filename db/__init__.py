from flask_sqlalchemy import SQLAlchemy
from .db import db  # `db.py` を相対パスでインポート

db = SQLAlchemy()
