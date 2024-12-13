from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from db.connection import configure_database, db  # 修正: db と configure_database をインポート
from routes.queue.add import queue_add_bp
from routes.queue.leave import queue_leave_bp
from routes.queue.status import queue_status_bp
from routes.queue.prime_1 import queue_prime_bp
from routes.wait_time import wait_time_bp
import os

# 環境変数をロード
load_dotenv()

# Flaskアプリケーションを作成
app = Flask(__name__)

# CORS の設定
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://tech0-gen-8-step3-app-node-6.azurewebsites.net",
            "http://localhost:3000"
        ]
    }
})

# データベース設定
configure_database(app)  # データベース設定と初期化を一元化

# マイグレーションの設定
migrate = Migrate(app, db)  # Migrate の初期化はここで実施

# テスト用ルート
@app.route('/')
def home():
    return "Hello, World!!!!"

# Blueprint を登録
app.register_blueprint(queue_add_bp, url_prefix='/api')
app.register_blueprint(queue_leave_bp, url_prefix='/api')
app.register_blueprint(queue_status_bp, url_prefix='/api')
app.register_blueprint(queue_prime_bp, url_prefix='/api')
app.register_blueprint(wait_time_bp, url_prefix='/api')

# アプリケーションのエントリーポイント
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Azure が指定するポートを使用
    app.run(debug=False, host="0.0.0.0", port=port)
