from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from db.connection import configure_database, db  # db と configure_database をインポート
from routes.queue.add import queue_add_bp
from routes.queue.leave import queue_leave_bp
from routes.queue.status import queue_status_bp
from routes.queue.prime_1 import queue_prime_bp
from routes.wait_time import wait_time_bp
import os
import logging

# 環境変数をロード
load_dotenv()

# Flaskアプリケーションを作成
app = Flask(__name__)

# ロギング設定（デバッグ用）
logging.basicConfig(level=logging.DEBUG)

# CORS の設定
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://tech0-gen-8-step3-app-node-6.azurewebsites.net",
            "http://localhost:3000"
        ],
        "supports_credentials": True
    }
})

# データベース設定
try:
    configure_database(app)  # データベース設定と初期化を一元化
except Exception as e:
    app.logger.error(f"Failed to configure database: {e}")

# マイグレーションの設定
try:
    migrate = Migrate(app, db)  # Migrate の初期化はここで実施
except Exception as e:
    app.logger.error(f"Failed to initialize migrations: {e}")

# エラー処理（500 Internal Server Error 対応）
@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"An unexpected error occurred: {e}")
    return jsonify({"error": "Internal Server Error"}), 500

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
    try:
        port = int(os.getenv("PORT", 8080))  # Azure が指定するポートを使用
        app.run(debug=False, host="0.0.0.0", port=port)
    except Exception as e:
        app.logger.error(f"Failed to start application: {e}")
