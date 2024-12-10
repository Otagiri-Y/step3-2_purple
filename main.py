from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from db import db  # 修正: db を専用モジュールからインポート
from routes.queue.add import queue_add_bp
from routes.queue.leave import queue_leave_bp
from routes.queue.status import queue_status_bp
from routes.queue.prime_1 import queue_prime_bp
from routes.wait_time import wait_time_bp

# 環境変数をロード
load_dotenv()

# Flaskアプリケーションを作成
app = Flask(__name__)

# データベース設定
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?ssl_ca={os.getenv('DB_SSL_CA')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# データベース初期化
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Hello, World!!!!"

# Blueprintを登録
app.register_blueprint(queue_add_bp, url_prefix='/api')
app.register_blueprint(queue_leave_bp, url_prefix='/api')
app.register_blueprint(queue_status_bp, url_prefix='/api')
app.register_blueprint(queue_prime_bp, url_prefix='/api')
app.register_blueprint(wait_time_bp, url_prefix='/api')

# アプリケーションのエントリーポイント
if __name__ == "__main__":
    app.run(debug=True)