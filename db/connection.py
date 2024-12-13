import os
import tempfile
import logging
import atexit
from db import db  # db/__init__.py からインポート

# ログの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SSL証明書を含むデータベース設定を行う関数
def configure_database(app):
    """
    Flaskアプリケーションにデータベース設定を追加する関数。
    環境変数からデータベース接続情報とSSL証明書を取得。
    """
    try:
        # データベースURLを環境変数から作成
        DATABASE_URL = (
            f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        )

        # SSL証明書の内容を環境変数から取得
        pem_content = os.getenv("DB_SSL_CA")
        if pem_content:
            # 改行コード（\n）を元の改行に戻す
            pem_content = pem_content.replace("\\n", "\n")
            # 一時ファイルを作成し、SSL証明書を保存
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".pem") as temp_pem:
                temp_pem.write(pem_content)
                temp_pem_path = temp_pem.name

            # アプリケーション終了時に一時ファイルを削除
            atexit.register(lambda: os.unlink(temp_pem_path))

            # データベースURLにSSL設定を追加
            DATABASE_URL += f"?ssl_ca={temp_pem_path}"
        else:
            logger.error("SSL証明書の環境変数 DB_SSL_CA が設定されていません。")
            raise ValueError("SSL証明書の環境変数 DB_SSL_CA が設定されていません。")

        # FlaskアプリケーションにデータベースURIを設定
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    except Exception as e:
        logger.error(f"データベース設定中にエラーが発生しました: {e}")
        raise
