import sqlite3

DATABASE = "queue_app.db"

def get_db_connection():
    """SQLite データベース接続を取得"""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row  # 辞書形式で結果を取得
    return connection
