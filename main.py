from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from db.connection import db, configure_database  # 修正済み: connection.py からインポート
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

# データベースの設定（SSL証明書処理を含む）
configure_database(app)

# CORSの設定（特定のオリジンを許可し、クレデンシャルをサポート）
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://tech0-gen-8-step3-app-node-6.azurewebsites.net"]
    }
}, supports_credentials=True)

# プリフライトリクエストやレスポンスにCORSヘッダーを明示的に追加
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://tech0-gen-8-step3-app-node-6.azurewebsites.net"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response

# OPTIONS メソッドに対応
@app.route('/api/<path:path>', methods=['OPTIONS'])
def handle_options(path):
    response = jsonify({"message": "CORS preflight success"})
    response.headers["Access-Control-Allow-Origin"] = "https://tech0-gen-8-step3-app-node-6.azurewebsites.net"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response

# Flask-Migrateの初期化
migrate = Migrate(app, db)

# テスト用エンドポイント
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
    port = int(os.getenv("PORT", 8080))  # Azureが指定するポートを使用
    app.run(debug=False, host="0.0.0.0", port=port)
