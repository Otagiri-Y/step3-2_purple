from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from db import db, configure_database  # db と SSL 設定を行う関数をインポート
from routes.queue.add import queue_add_bp
from routes.queue.leave import queue_leave_bp
from routes.queue.status import queue_status_bp
from routes.queue.prime_1 import queue_prime_bp
from routes.wait_time import wait_time_bp
import os

# 環境変数をロード（.envファイルがある場合はローカルで読み込む）
load_dotenv()

# Flaskアプリケーションを作成
app = Flask(__name__)

# CORSの設定（特定のドメインからのリクエストのみ許可）
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://tech0-gen-8-step3-app-node-6.azurewebsites.net",
            "http://localhost:3000"
        ],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# データベースの設定（SSL証明書処理含む）を実行
configure_database(app)

# Flask-Migrate の初期化（データベースのマイグレーション管理用）
migrate = Migrate(app, db)

# ルートの設定（テスト用）
@app.route('/')
def home():
    return "Hello, World!!!!"

# Blueprintを登録して各エンドポイントを分割管理
app.register_blueprint(queue_add_bp, url_prefix='/api')
app.register_blueprint(queue_leave_bp, url_prefix='/api')
app.register_blueprint(queue_status_bp, url_prefix='/api')
app.register_blueprint(queue_prime_bp, url_prefix='/api')
app.register_blueprint(wait_time_bp, url_prefix='/api')

# アプリケーションのエントリーポイント
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Azureが指定するポートを使用
    app.run(debug=False, host="0.0.0.0", port=port)  # 本番環境では debug=False
